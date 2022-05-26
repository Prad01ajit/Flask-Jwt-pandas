
from flask import Blueprint , jsonify
from .auth import token_required
import pandas as pd

#Fetching and manipulating Airquality Index Data
aqi_blueprint = Blueprint('aqi_blueprint', __name__)\

df = pd.read_csv("/home/pradeep/Downloads/AQIDay.csv",usecols=["City","AQI"])
dfh = pd.read_csv("/home/pradeep/Downloads/AQIData.csv",usecols=["City","Date","AQI"])


@aqi_blueprint.route('/top-3',methods = ['GET'])
@token_required
def top_cities(self):
     _sortdesc = df.sort_values(["AQI"], ascending= False)
     _slicedesc = _sortdesc[0:3]
     return jsonify({"Polluted cities" : _slicedesc.City.to_string(index=False)})


@aqi_blueprint.route('/bottom-3',methods = ['GET'])
@token_required
def bottom_cities(self):
    _sortaesc =  df.sort_values(["AQI"], ascending= True)
    _sliceaesc = _sortaesc[0:3]
    return jsonify({"Clean Cities" : _sliceaesc.City.to_string(index=False)})











