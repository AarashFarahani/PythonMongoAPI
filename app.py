from flask import Flask
from flask import request
from pymongo import MongoClient
from bson.json_util import dumps
import json

client = MongoClient('localhost:27017')
db = client.DataDB

app = Flask(__name__)

@app.route("/add", methods = ['POST'])
def add():
    try:
        data = json.loads(request.data)
        print(data)
        
        if(data):
            db.Data.insert_one(data);

        return dumps({'message' : 'SUCCESS'})
    except Exception as e:
        return dumps({'error' : str(e)})

@app.route("/getAll", methods = ['GET'])
def getAll():
    try:
        data = db.Data.find()
        return dumps(data)
    except Exception as e:
        return dumps({'error' : str(e)})

if __name__ == "__main__":
    app.run()