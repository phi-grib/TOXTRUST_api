from flask import request,json,send_file
from settings import *
from toxtrust import flask
import json

# GET EVIDENCE RESULT
@app.route(f'{url_base}{version}evidence_result/<string:endpoint_name>/<string:evidence_name>',methods=['GET'])
@cross_origin()
def getEvidenceResult(endpoint_name,evidence_name):
    success,data = flask.returnComputedResult(endpoint_name,evidence_name)
    return json.dumps({'success':success,'data':data}),200,{'ContentType':'application/json'}

#DELETE EVIDENCE
@app.route(f'{url_base}{version}delete_evidence/<string:endpoint_name>/<string:evidence_name>',methods=['DELETE'])
@cross_origin()
def deleteEvidence(endpoint_name,evidence_name):
    success,data = flask.removeEvidence(endpoint_name,evidence_name)
    return json.dumps({'success':success,'data':data}),200,{'ContentType':'application/json'}

#GET EVIDENCE IMAGE PATH
@app.route(f'{url_base}{version}evidence_image_path/<string:endpoint_name>/<string:evidence_name>',methods=['GET'])
@cross_origin()
def getEvidenceImagePath(endpoint_name,evidence_name):
    success,data = flask.pathEvidencePlot(endpoint_name,evidence_name)
    if success:
        return send_file(data,as_attachment=True)
    else:
        return json.dumps(f'Failed to get link'), 500, {'ContentType':'application/json'} 


# GET COMBINATION IMAGE PATH
@app.route(f'{url_base}{version}combination_image_path/<string:endpoint_name>/<string:evidence_name>',methods=['GET'])
@cross_origin()
def getCombinationImagePath(endpoint_name):
    success,data = flask.pathCombinationPlot(endpoint_name)
    if success:
        return send_file(data,as_attachment=True)
    else:
        return json.dumps(f'Failed to get link'), 500, {'ContentType':'application/json'} 

