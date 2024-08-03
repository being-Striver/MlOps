import pickle
from flask import Flask, request, render_template
import numpy as np 
import pandas as pd


application=Flask(__name__)
app=application()


#route for homepage

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/prediction', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else :
        pass