from flask import Flask
import google-cloud-bigquery as bq

app = Flask(__name__)


@app.route('/')
def hello_world():
    greeting = '{"greeting":"hello world"}'
    return greeting


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
