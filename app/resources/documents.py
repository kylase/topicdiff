import os
from collections import defaultdict
from flask_restful import Resource, reqparse
from flask import current_app
from app.common.topic_model import TopicModelPipeline

parser = reqparse.RequestParser()

parser.add_argument('content', action='append', required=True)
parser.add_argument('model', type=str, choices=('wikipedia',), trim=True, default='wikipedia')
parser.add_argument('threshold', type=float, default=0.01)

class Compare(Resource):
    def post(self):
        """
        Submit 1 or more `content`
        """
        args = parser.parse_args()
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