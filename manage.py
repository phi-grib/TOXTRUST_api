from flask import request,json
from settings import *
from toxtrust import manage
from toxtrust import flask
from functions import *
import json

# GET LIST OF ENDPOINTS
@app.route(f'{url_base}{version}list',methods=['GET'])
@cross_origin()
def getListEndpoints():
    data = manage.listEndpointsDetails()
    return data

# GET ENDPOINT
@app.route(f'{url_base}{version}endpoint_data/<string:endpoint_name>',methods=['GET'])
@cross_origin()
def getEndpointInformation(endpoint_name):
    success,data = flask.returnEndpointContent(endpoint_name)
    return json.dumps({'success':success,'data':data}),200,{'ContentType':'application/json'}

# GET EVIDENCES
@app.route(f'{url_base}{version}evidences/<string:endpoint_name>',methods=['GET'])
@cross_origin()
def getEvidences(endpoint_name):
    success,data = flask.returnEvidenceInput(endpoint_name)
    dataFormatted = addProbabilities(endpoint_name,data)
    return json.dumps({'success':success,'data':dataFormatted}),200,{'ContentType':'application/json'}

#CREATE ENDPOINT
@app.route(f'{url_base}{version}new/<string:endpoint_name>',methods=['POST'])
@cross_origin()
def createEndpoint(endpoint_name):
    manage.createEndpoint(endpoint_name)
    return json.dumps({'success':True}),200,{'ContentType':'application/json'}

#DELETE ENDPOINT
@app.route(f'{url_base}{version}delete_endpoint/<string:endpoint_name>',methods=['DELETE'])
@cross_origin()
def deleteEndpoint(endpoint_name):
    success,data = manage.removeEndpoint(endpoint_name)
    return json.dumps({'success':success,'data':data}),200,{'ContentType':'application/json'}

#CALL ENDPOINT INPUT
@app.route(f'{url_base}{version}call_endpoint_input/<string:endpoint_name>',methods=['POST'])
@cross_origin()
def callEndpointInput(endpoint_name):
    data = request.get_json()
    success, message = flask.callEndpointInput(endpoint_name,data)

    return json.dumps({'success':success,'message':message}),200,{'ContentType':'application/json'}

# CALL EVIDENCE INPUT
@app.route(f'{url_base}{version}call_evidence_input/<string:endpoint_name>',methods=['POST'])
@cross_origin()
def callEvidenceInput(endpoint_name):
    data = request.get_json()
    success,message = flask.callEvidenceInput(endpoint_name,data)

    return json.dumps({'success':success,'message':message}),200,{'ContentType':'application/json'}


# CALL DECISION INPUT
@app.route(f'{url_base}{version}call_decision_input/<string:endpoint_name>',methods=['POST'])
@cross_origin()
def callDecisionInput(endpoint_name):
    data = request.get_json()
    success,message = flask.callDecisionInput(endpoint_name,data)
    return json.dumps({'success':success,'message':message}),200,{'ContentType':'application/json'}
