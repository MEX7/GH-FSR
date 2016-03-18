from flask import Flask
import os

app = Flask(__name__)


@app.route('/script/oerp/v1/java/reload', methods='POST')
def oerp_java_reload():
    os.system('bash ./sh/java/oerp_v1_reload.sh')
    return '/script/oerp/v1/java/reload'


@app.route('/script/oerp/v1/web/reload', methods='POST')
def oerp_web_world():
    os.system('bash ./sh/web/oerp_v1_reload.sh')
    return '/script/oerp/v1/web/reload'

if __name__ == '__main__':
    # app.debug = True
    app.run(host='0.0.0.0')
