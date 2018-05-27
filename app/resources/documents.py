import os
from collections import defaultdict
from flask_restful import Resource, reqparse
from flask import current_app
from app.common.topic_model import TopicModelPipeline

parser = reqparse.RequestParser()

parser.add_argument('content', action='append')

class Compare(Resource):
    def post(self):
        """
        """
        args = parser.parse_args()

        model_type = args.get('model', 'wiki')

        pipeline = TopicModelPipeline(
            os.path.join(current_app.config.get('MODELS_DIR'), model_type, 'tf'), 
            os.path.join(current_app.config.get('MODELS_DIR'), model_type, 'lda')
        )
        
        metadata = {
            'data': defaultdict(dict)
        }

        for i, doc in enumerate(args['content']):
            metadata['data'][str(i)]['content'] = doc
            topics = sorted(pipeline.infer(doc), key=lambda x: x[1], reverse=True)
            metadata['data'][str(i)]['topics'] = [{'topic_id': t, 'distribution': float(s)} for t, s in topics]

        return metadata