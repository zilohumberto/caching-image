from flask import Flask, jsonify, request
from flask_restful import Api
from services import LoadImageService, GetImageService
from settings import DEVELOPMENT_API_HOST, DEVELOPMENT_API_PORT, DEVELOPMENT_API_DEBUG

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.url_map.strict_slashes = False
api = Api(app, prefix="/")

"""
    Load and images from service
"""
loadImageService = LoadImageService()


@app.route('/')
def ping():
    return 'Pong'


@app.route('/search/')
def search(**kwargs):
    query_string = request.query_string
    return jsonify(GetImageService.search(query_string))


if __name__ == '__main__':
    app.run(
        host=DEVELOPMENT_API_HOST,
        port=DEVELOPMENT_API_PORT,
        debug=DEVELOPMENT_API_DEBUG
    )
