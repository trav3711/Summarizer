from flask import Flask, jsonify, request, render_template
import requests, json
import summarizer as s

app = Flask(__name__)

@app.route("/", methods=['GET'])
def main():
    return render_template('index.html', summary="")

@app.route('/', methods = ['POST'])
def summary_main():
    text = request.form['input_text']
    length = request.form['summary_length']
    summary_text = s.summarize(text, int(length))
    return render_template('index.html', summary=summary_text)

@app.route("/rest", methods=['GET', 'POST'])
def rest_main():
    r = json.loads(request.data)
    length = r['summary_length']
    summary = s.summarize(r['text'], int(length))
    payload = {
        "summary": summary
    }
    return payload

gunicorn --chdir app main:app -w 2 --threads 2 -b 0.0.0.0:8003
