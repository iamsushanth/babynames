import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    if request.method == 'POST':
        dob = request.form.get('DOB')
        digits = dob.replace('-', '').strip()
        day = digits[6:]
        day = str(day)
        bd = sum(int(i) for i in day)

        x = str(digits)
        n = sum(int(i) for i in x)
        n = str(n)
        lf = sum(int(x) for x in n)


        prediction = model.predict([[lf,bd]])


    return render_template('index.html', name='Name Number {} Birthday Number {} Life Path Number {}'.format(prediction,bd,lf))


if __name__ == "__main__":
    app.run(debug=True)