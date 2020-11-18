from flask import Flask, render_template, request
from flask_restful import Resource, Api
import json
import summarize as s

app = Flask(__name__)

@app.route('/')
def test():
    return 'why are you here? I feel violated.'

@app.route('/webhook', methods=['POST'])
def webhook():
    webhook_message = json.loads(request.data)

    article_text = webhook_message["text"]

    summary = s.Summarize(article_text, 5)

    return {
        'summary':summary
    }
