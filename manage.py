from settings import *
from toxtrust import manage

# GET LIST OF ENDPOINTS
@app.route(f'{url_base}{version}list',methods=['GET'])
@cross_origin()
def getListEndpoints():
    data = manage.listEndpoints()
    print(data)
    return data