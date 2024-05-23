from flask import Flask
from manage import *


@app.route('/')
def hello_world():
    return '¡Hola, Mundo!'

if __name__ == '__main__':
    app.run(debug=True,port=5000)