from flask import request,json,send_file
from settings import *
from toxtrust import flask
import json


# SELECT RULE
@app.route(f'{url_base}{version}select_rule/<string:endpoint_name>',methods=['POST'])
@cross_origin()
def selectRule(endpoint_name):
    data = request.get_json()
    factor = data.get('factor')
    success,message = flask.selectRule(endpoint_name,data['rule'],factor)
    return json.dumps({'success':success,'message':message}),200,{'ContentType':'application/json'}

# SHOULD COMBINE INPUT
@app.route(f'{url_base}{version}should_combine/<string:endpoint_name>',methods=['POST'])
@cross_origin()
def callCombinationInput(endpoint_name):
    listEvidences = request.get_json()
    success,message = flask.shouldCombineInput(endpoint_name,listEvidences)
    return json.dumps({'success':success,'message':message}),200,{'ContentType':'application/json'}


