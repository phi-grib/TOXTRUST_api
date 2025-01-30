from flask import Flask
from manage import *
from evidence import *
from combination import *
@app.route('/')
def hello_world():
    return "TOXTRUST"

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)