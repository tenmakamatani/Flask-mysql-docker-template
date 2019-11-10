from flask import Flask, jsonify

from flask_restful import Api

import os

from controllers.InformationController import InformationController

def create_app():

    app = Flask(__name__)

    api = Api(app)
    api.add_resource(InformationController, '/informations')

    return app

app = create_app()

@app.route('/test', methods=['GET'])
def test():
    return 'ok'

PORT = int(os.environ.get('PORT'))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)
