from flask import Flask, jsonify, request
import pandas as pd
import numpy as np
import joblib,pickle
import traceback
from flask_restful import reqparse
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "hey"

@app.route('/predict/', methods=['POST'])
def predict():
	#model = joblib.load("model.pkl")
	#if model:
	#	try:
			# json = request.get_json()	 
			# temp=list(json[0].values())
			# vals=np.array(temp)
			# prediction = model.predict(temp)
			# print("here:",prediction)        
			# return jsonify({'prediction': str(prediction[0])})
	#model = joblib.load("model.pkl")
	model = pickle.load(open('model.pkl','rb'))
	data = request.get_json()
	prediction = np.array2string(model.predict(data))
	return jsonify(prediction)

if __name__ == '__main__':
	#model = joblib.load("model.pkl")
	model = pickle.load(open('model.pkl','rb'))
	app.run(debug=True)