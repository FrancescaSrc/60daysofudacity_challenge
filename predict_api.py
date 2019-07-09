from flask import Flask, request 
from keras.models import load_model
from keras import backend as K

import numpy 
app = Flask(__name__)
@app.route('/') 
def hello_world(): 
    return 'Housing price predict app'


@app.route('/predict', methods=['POST']) 
def add():
    req_data = request.get_json()
    bizprop = req_data['bizprop'] 
    rooms = req_data['rooms'] = 1
    age = req_data['age'] = 1
    highways = req_data['highways'] =1
    tax = req_data['tax'] = 1
    ptratio = req_data['ptratio'] =1
    lstat = req_data['lstat'] =1
    # This is where we load the actual saved model into new variable. 
    deep_and_wide_net = load_model('deep_and_wide_net.h5') 
    # Now we can use this to predict on new data 
    value = deep_and_wide_net.predict_on_batch(numpy.array([[bizprop, rooms, age, highways, tax, ptratio, lstat]], dtype=float)) 
    K.clear_session()

    return str(value)