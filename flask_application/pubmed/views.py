from .models import new
from flask import Flask, request, session, redirect, url_for, render_template, flash
import pandas as pd

#import wtforms

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pubmed.html')

@app.route('/bibs')
def bibs():
    _items = db.bibsdb.find()
    items = [item for item in _items]

    return render_template('index.html', items=items)
	