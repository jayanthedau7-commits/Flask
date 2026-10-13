    
from flask import Flask, render_template, request
from datetime import datetime
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()


MONGO_URL = os.getenv('MONGO_URL')

client = pymongo.MongoClient(MONGO_URL)

db = client.test

collection  = db['Flask_tutorial']

MONGO_URI = os.getenv('MONGO_URI')

client = pymongo.MongoClient(MONGO_URI)

app = Flask(__name__)



@app.route ( '/submit' , methods=['POST'])
def submit():
    
    form_data = dict(request.form)
    
    collection.insert_one(form_data)
    
    print(form_data)
    
    return 'Data submitted succesfully !!'

@app.route('/view')
def view():
    
    data = collection.find()
    
    data = list(data)
    
    for item in data:
           
           print(item)
    
    del item['_id']
    
    data = {
        'data':data
    }
    
    return data


if __name__ == '__main__':
    app.run( host='0.0.0.0',port=9000,debug=True)
    
    