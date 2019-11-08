from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    return 'test'

PORT = int(os.environ.get('PORT'))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)