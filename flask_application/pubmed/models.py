from flask import Flask, redirect, url_for, request, render_template
from flask_pymongo import PyMongo
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.mlab as mlab
from pylab import *
from wordcloud import WordCloud
import csv

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

def new():
    item_doc = {
        'name': request.form['name'],
        'description': request.form['description']
    }
    mongo.db.bibsdb.insert_one(item_doc)

    return redirect(url_for('bibs'))

def word_cloud():
    d = {}
    with open('./pubmed/static/data/meshcount.csv', newline='\n') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='|')
        for k,v in spamreader:
            d[k] = int(v)
        
    wordcloud = WordCloud(background_color='white',margin=10)
    wordcloud = wordcloud.generate_from_frequencies(d)
#    wordcloud.recolor(color_func = grey_color_func)
    plt.figure()
#    ax = Axes(plt.gcf(),[0,0,1,1],yticks=[],xticks=[],frame_on=False)
#    plt.gcf().delaxes(plt.gca())
#    plt.gcf().add_axes(ax)
    plt.imshow(wordcloud, interpolation="bilinear")
#    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig('pubmedplus_wordcloud.png', bbox_inches="tight", pad_inches=0)