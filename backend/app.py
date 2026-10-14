from flask import Flask, render_template, request, jsonify
from datetime import datetime
from dotenv import load_dotenv
import json
import os
import pymongo

load_dotenv()

MONGO_URL = os.getenv('MONGO_URL')

client = pymongo.MongoClient(MONGO_URL)

db = client.test

collection = db['Flask_tutorial']

todo_collection = db['todo_items']

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'data.json')


@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.form)
    collection.insert_one(form_data)
    print(form_data)
    return 'Data submitted succesfully !!'


@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    data = request.form or request.get_json(silent=True) or {}

    item_name = str(data.get('itemName', '')).strip()
    item_description = str(data.get('itemDescription', '')).strip()

    if not item_name or not item_description:
        return 'itemName and itemDescription are required.', 400

    todo_collection.insert_one({
        'itemName': item_name,
        'itemDescription': item_description
    })

    return 'To-Do item saved successfully !!'


@app.route('/view')
def view():
    data = list(collection.find())

    for item in data:
        del item['_id']

    return {'data': data}


@app.route('/api')
def api():
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)