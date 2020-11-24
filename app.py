from flask import Flask, jsonify, Request, request, render_template
import requests, json
import summarizer as s

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/summary', methods = ['POST'])
def summary_main():
    text = request.form['input_text']
    length = request.form['summary_length']
    summary_text = s.summarize(text, int(length))
    return render_template('summary.html', result=summary_text)


if __name__ == '__main__':
    app.run(debug=True)
