import pandas as pd
import numpy as np
from flask import Flask, render_template, Response, request
import pickle
from sklearn.preprocessing import LabelEncoder, StandardScaler
import pickle

app = Flask(__name__)
filename = 'resale.nav'
model_rand = pickle.load(open(filename, 'rb'))
ss = StandardScaler()


@app.route('/')
def index():
    return render_template('secpage.html')


@app.route('/y_predict', methods=['GET', 'POST'])
def y_predict():
    if request.method == "POST":
        seller = request.form['seller']
        offer_type = request.form['offerType']
        kms = request.form['kms']
        gearbox = request.form['gearbox']
        absets = request.form['abset']
        vehicle_type = request.form['model']
        fueltype = request.form['fuel']
        registration = 2022 - int(request.form['fuel'])
        kms = ss.fit_transform([[kms]])
        value = model_rand.predict([[seller, offer_type, absets, vehicle_type, registration, gearbox, fueltype, kms]])
        return render_template('output.html', flag=True, y_prd=round((ss.inverse_transform([value])[0][0]), 2))


if __name__ == '__main__':
    app.run(debug=True)