from __future__ import annotations
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)#our flask app
model = pickle.load(open('fbgold.pkl', 'rb')) #loading the model

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')#rendering html page

@app.route('/GoldPrice',methods=['POST','GET'])
def prediction(): # route which will take you to the prediction page
    return render_template('predict.html')

future = model.make_future_dataframe(periods = 365)
forecast = model.predict(future)
@app.route('/predict',methods=['POST'])
def y_predict():
    if request.method == "POST":
        ds = request.form["Date"]
        print(ds)
        
        ds=str(ds)
        print(ds)
        next_day=ds
        print(next_day)
        prediction=forecast[forecast['ds'] == next_day]['yhat'].item()
        
        print(prediction)
        #print(prediction[0])
        output=round(prediction,2) #rounding off the decimal values to 2
        print(output)
        return render_template('predict.html',prediction_text="Gold Commodity Price on selected date is $ {} Cents".format(output))
    return render_template("predict.html")
    
if __name__ == "__main__":
    app.run(debug=False)
