from evidence import *
from toxtrust import flask
def addProbabilities(endpoint_name,data):
    selection = "probabilities"
    listNameEvidences = list(data.keys())
    for evidence in listNameEvidences:
        success,result = flask.returnComputedResult(endpoint_name,evidence,selection)
        if success:
            data[evidence][selection] = result
    return data
