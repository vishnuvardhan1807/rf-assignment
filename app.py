from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import pickle

# initialize the Flask app
app = Flask(__name__)


@app.route('/', methods=['GET'])
@cross_origin()
def homepage():
    return render_template('index.html')


# route to show predictions
@app.route('/predict', methods=['GET', 'POST'])
@cross_origin()
def predict():
    if request.method == "POST":
        try:
            # reading the input values
            CRIM = float(request.form["CRIM"])
            ZN = float(request.form["ZN"])
            INDUS = float(request.form["INDUS"])
            CHAS = float(request.form["CHAS"])
            NOX = float(request.form["NOX"])
            RM = float(request.form["RM"])
            AGE = float(request.form["AGE"])
            DIS = float(request.form["DIS"])
            RAD = float(request.form["RAD"])
            TAX = float(request.form["TAX"])
            PTRATIO = float(request.form["PTRATIO"])
            B = float(request.form["B"])
            LSTAT = float(request.form["LSTAT"])

            # open the model
            filename = 'model.pickle'
            loaded_model = pickle.load(open(filename, 'rb'))

            # make predictons
            predictions = loaded_model.predict([[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS,
                                                 RAD, TAX, PTRATIO, B, LSTAT]])

            return render_template('result.html', prediction=predictions[0])

        except Exception as e:
            return "something is wrong"
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
