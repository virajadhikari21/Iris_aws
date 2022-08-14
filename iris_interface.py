from flask import Flask, jsonify,redirect,request,render_template
from predict import predict_class

app = Flask(__name__)

# @app.route('/')
# def hello_flask():
#     print('*'*90)
#     print("We are testing Flask")
#     print('*'*90)
#     return jsonify({"Message" : "Welcome to Flask"})

# @app.route('/test')
# def test():
#     '''
#     ---- TEST API ----
#     This is Testing API 
#     '''

#     print("This is Testing API")
#     return jsonify({"Message" : "Test API Successful"})

################ Root API ########################################
@app.route('/')
def man():
    return render_template('home.html')

############################################################################
######################## Addition API ######################################
############################################################################

@app.route('/predict',methods = ["GET",'POST'])
def predict():
    if request.method == 'POST':
        data =request.get_json() 
        print("data :::::::::",data)
        SepalLengthCm = float(data['SepalLengthCm'])
        SepalWidthCm = float(data['SepalWidthCm'])
        PetalLengthCm = float(data['PetalLengthCm'])
        PetalWidthCm = float(data['PetalWidthCm'])

        x_new=[[SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm]]

        predict_value_1 = predict_class(x_new)

        print('*'*50)
        print('hello')
        print('*'*50)
        
        return jsonify({"Result": predict_value_1})

    else:
        return jsonify({"Message":"Not Successful"})


if __name__ == '__main__':
    app.run(host = '0.0.0.0')
