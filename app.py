from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import summarizer as s

app = Flask(__name__)
api = Api(app)

class Summary(Resource):
    def get(self):
        text = request.json['text']
        summary_length = request.json['summary_length']
        summary_text = s.summarize(text, summary_length)

        return {'summary': summary_text}

api.add_resource(Summary, '/summary')

if __name__ == '__main__':
    app.run(debug=True)
