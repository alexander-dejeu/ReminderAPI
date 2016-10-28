from flask import Flask, request, json, jsonify
import pymongo
from pymongo import MongoClient

# client = MongoClient - local host
client = MongoClient('https://murmuring-coast-74546.herokuapp.com/:27017')
db = client['primer']
app = Flask(__name__)

tasks = db['task']


@app.route('/')
def home():
    return 'Hello World'


@app.route('/tasks', methods=['GET', 'PUT'])
def tasks():
    if request.method == 'GET':
        return 'getting stuff'
    elif request.method == 'PUT':
        return 'putting it here'


@app.route('/tasks/<id>', methods=['GET', 'DELETE'])
def getTask(id):
    if request.method == 'GET':
        return 'getting user @ id'
    elif request.method == 'DELETE':
        return 'this user is about to be hella deleted'


if __name__ == '__main__':
    app.run()
