from flask import Flask
from flask_cors import CORS, cross_origin

UPLOAD_FOLDER = './'
app = Flask(__name__,static_folder="static/dist",static_url_path="/")
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
url_base = "/toxtrust/"
version = "v1/"
