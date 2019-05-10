from .models import new, word_cloud
from flask import Flask, request, session, redirect, url_for, render_template, flash
import pandas as pd

#import wtforms

app = Flask(__name__)

@app.route('/')
def index():
#    word_cloud()
    return render_template('pubmed.html')


@app.route('/CMView', methods=['GET','POST'])
def result_list():
    if request.method == 'POST':
        SearchPhrase = request.form['SearchPhrase']
        MeshTerms = request.form['MeshTerms']
        PublicationYear = request.form['PublicationYear']
        Gender = request.form['Gender']
        
        data = pd.DataFrame({'SearchPhrase':SearchPhrase,'MeshTerms':MeshTerms, 'PublicationYear':PublicationYear, 'Gender':Gender}, index=[0])
#        annotation(data)
    return render_template('result-list.html')

@app.route('/bibs')
def bibs():
    _items = db.bibsdb.find()
    items = [item for item in _items]

    return render_template('index.html', items=items)
	