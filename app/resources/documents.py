import os
from collections import defaultdict
from flask_restful import reqparse
from flask_restful_swagger_2 import swagger, Resource
from flask import current_app
from app.resources.schemas import CompareRequestBody
from app.common.topic_model import TopicModelPipeline

class Compare(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('content', action='append', required=True)
    parser.add_argument('model', type=str, choices=('wikipedia',), trim=True, default='wikipedia')
    parser.add_argument('threshold', type=float, default=0.01)

    @swagger.doc({
        'tags': ['Documents'],
        'description': 'Infer the topics which the document(s) is/are associated to.',
        'parameters': [
            {
                'description': 'Content that is/are going to be parsed and inferred by the topic model with certain threshold.',
                'in': 'body',
                'name': 'body',
                'required': True,
                'schema': CompareRequestBody
            }
        ],
        'responses': {
            '200': {
                'description': 'Successfully parsed the document(s) and inferred the topics.',
                'examples': {
                    'application/json': {
                        "data": {
                            "1": {
                                "0": 0.17226679623126984,
                                "1": 0.08550900220870972
                            },
                            "10": {
                                "0": 0.08550900220870972
                            },
                            "77": {
                                "0": 0.07097268104553223
                            }
                        },
                        "model": {
                            "name": "wikipedia",
                            "total_topics": 100,
                            "threshold": 0.05
                        }
                    }
                }
            },
            '400': {
                'description': 'Body is not valid, such as no content is included in the body or model is not valid or threshold is out of range.'
            }
        }
    })

    def post(self):
        args = self.parser.parse_args()
        model_type = args.get('model')
        threshold = args.get('threshold')

        pipeline = TopicModelPipeline(
            os.path.join(current_app.config.get('MODELS_DIR'), model_type, 'tf'), 
            os.path.join(current_app.config.get('MODELS_DIR'), model_type, 'lda')
        )
        
        response = {
            'data': defaultdict(dict),
            'model': {
                'name': model_type,
                'total_topics': pipeline.lda.num_topics,
                'threshold': threshold
            }
        }

        for i, doc in enumerate(args['content']):
            doc_topics = pipeline.infer(doc)
            for t, s in doc_topics:
                if s >= threshold:
                    response['data'][t].update({i: float(s)})
    
        return response