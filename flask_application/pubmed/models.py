from flask import Flask, redirect, url_for, request, render_template
#from pymongo import MongoClient
import os
from flask_pymongo import PyMongo

app = Flask(__name__)

#client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
#db = client.bibsdb

app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

def new():

    item_doc = {
        'name': request.form['name'],
        'description': request.form['description']
    }
    mongo.db.bibsdb.insert_one(item_doc)

    return redirect(url_for('bibs'))