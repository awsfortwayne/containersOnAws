import requests
from flask import Flask


app = Flask(__name__)




@app.route('/api')
def hello():
    return "Hello FW AWS User Group!"

@app.route('/api/health')
def healthcheck():
    return "Success"

@app.route('/api/demo')
def callAnotherContainer():
    return requests.get('http://other-container/hello').content


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
