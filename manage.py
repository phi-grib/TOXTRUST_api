from settings import *
from toxtrust import manage
import json

# GET LIST OF ENDPOINTS
@app.route(f'{url_base}{version}list',methods=['GET'])
@cross_origin()
def getListEndpoints():
    data = manage.listEndpoints()
    print(data)
    return data

#CREATE ENDPOINT
@app.route(f'{url_base}{version}new/<string:endpoint_name>',methods=['PUT'])
@cross_origin()
def createEndpoint(endpoint_name):
    manage.createEndpoint(endpoint_name)
    return json.dumps({'success':True}),200,{'ContentType':'application/json'}

#DELETE ENDPOINT
@app.route(f'{url_base}{version}delete/<string:endpoint_name>',methods=['PUT'])
@cross_origin()
def deleteEndpoint(endpoint_name):
    manage.removeEndpoint(endpoint_name)
    return json.dumps({'success':True}),200,{'ContentType':'application/json'}

