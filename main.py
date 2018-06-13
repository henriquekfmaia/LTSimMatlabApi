from flask import Flask, request, url_for
from flask_cors import CORS
import json

import service_logic as l

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello World"

@app.route('/run_generated_code', methods=['POST'])
def run_generated_code():
    req_data = request.get_json()
    parameter_list = req_data['parameter_list']
    script = req_data['script']
    result = l.run_generated_code(parameter_list, script)
    return result

@app.route('/run_ciclor', methods=['POST'])
def run_ciclor():
    req_data = request.get_json()
    parameter_list = req_data['parameter_list']
    result = l.run_ciclor(parameter_list)
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)