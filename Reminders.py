from flask import Flask, request, json, jsonify
import pymongo
from pymongo import MongoClient

# client = MongoClient

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'

if __name__ == '__main__':
    app.run()
