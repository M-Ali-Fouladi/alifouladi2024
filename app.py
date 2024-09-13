from flask import Flask, request, jsonify
import os
import signal


app = Flask(__name__)

#  GET request foo --> response=bar
@app.route('/foo', methods=['GET'])
def foo():
    return 'bar'

# POST request ,response = hello [your name(here is Prabh)] according to the data parameter name 
@app.route('/hello', methods=['POST'])
def hello():
    data = request.json
    name = data.get('name', 'World')
    return f"Hello {name}!"

# GET request to kill the current container 
@app.route('/kill', methods=['GET'])
def kill():
    os.kill(1, signal.SIGTERM)  
    return "Container is being terminated..."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
