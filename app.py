from flask import Flask,render_template,request
import joblib
import numpy as np


model = joblib.load("cancermodel.pkl")
encoder= joblib.load("LabelEncoder.pkl")


app=Flask(__name__)

@app.route("/")
def myform():
    return render_template("cancer.html")

@app.route("/predict",methods=["POST"])
def predict():
    genetic_risk = float(request.form["genetic_risk"])
    air_pollution = float(request.form["air_pollution"])
    alcohol_use= float(request.form["alcohol_use"])
    smoking= float(request.form["smoking"])
    obesity_level= float(request.form["obesity_level"])

    feature = np.array([[genetic_risk,air_pollution,alcohol_use,smoking,obesity_level]])
    prediction = model.predict(feature)

    prediction_label= encoder.inverse_transform(prediction)[0]
    return render_template("cancer.html",Prediction_text=f"You have {prediction_label} cancer")

if __name__ == "__main__":
    app.run(debug=True)
