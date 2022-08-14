from flask import Flask, jsonify,redirect,request,render_template
from predict import predict_class
import numpy as np

# model = pickle.load(open('iri.pkl', 'rb'))


app = Flask(__name__)


@app.route('/')
def man():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def home():
    a = request.form['a']
    b = request.form['b']
    c = request.form['c']
    d = request.form['d']


    arr = np.array([[a, b, c, d]])

    predict_value_1 = predict_class(arr)
 
    #pred = model.predict(arr)

    return f'Flower type is : {predict_value_1}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)  