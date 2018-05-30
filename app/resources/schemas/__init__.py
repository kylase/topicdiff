from flask_restful_swagger_2 import Schema

class CompareRequestBody(Schema):
    type = 'object'
    properties = {
        'content': {
            'type': 'array',
            'format':'string'
        },
        'model': {
            'type': 'string',
            'enum': ['wikipedia']
        },
        'threshold': {
            'type': 'number',
            'minimum': 1e-8,
            'maximum': 1.0
        }
    }