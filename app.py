from flask import Flask
import os

app = Flask(__name__)

@app.route('/configValue', methods=['GET'])
def get_config_value():
    config_value = os.getenv('CONFIG_VALUE', 'defaultConfig')
    return config_value

@app.route('/secretValue', methods=['GET'])
def get_secret_value():
    secret_value = os.getenv('SECRET_VALUE', 'defaultSecret')
    return secret_value

@app.route('/envValue', methods=['GET'])
def get_env_value():
    env_value = os.getenv('ENV_VALUE', 'defaultEnv')
    return env_value

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
