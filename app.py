from flask import Flask
from manage import *
from evidence import *
from combination import *


@app.route("/")
@app.route("/<path:path>")
def serve_app(path="index.html"):
    return send_from_directory(app.static_folder, path)


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)