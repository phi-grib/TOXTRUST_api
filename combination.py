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

# RUN COMBINE
@app.route(f'{url_base}{version}run_combine/<string:endpoint_name>',methods=['GET'])
@cross_origin()
def runCombine(endpoint_name):
    success,message = flask.runCombine(endpoint_name)
    print("success:",success)
    print("message:",message)
    return json.dumps({'success':success,'message':message}),200,{'ContentType':'application/json'}


#PATH COMBINATION IMAGE
@app.route(f'{url_base}{version}combination_image_path/<string:endpoint_name>',methods=['GET'])
@cross_origin()
def getCombinationImagePath(endpoint_name):
    success,data = flask.pathCombinationPlot(endpoint_name)
    print("combination path")
    print(success)
    if success:
        return send_file(data,as_attachment=True)
    else:
        return json.dumps(f'Failed to get link'), 500, {'ContentType':'application/json'} 

#Weight of evidence
@app.route(f'{url_base}{version}WoEinput/<string:endpoint_name>/<string:WoE>',methods=['GET'])
@cross_origin()
def shouldWoeInput(endpoint_name,WoE):
    if WoE.lower() in ["true","1"]:
        WoE = True
    else:
        WoE = False
    success,message = flask.shouldWoeInput(endpoint_name,WoE)
    return json.dumps({'success':success,'message':message}),200,{'ContentType':'application/json'}

