
import pickle

from flask import Flask, request
app = Flask(__name__)

@app.route("/") # Decorator # home page url
def hello_world():
    return "<p>Hello, World! - Version 1</p>"


@app.route("/ping",methods = ["GET"]) # home page/ping # Default method will be Get
def pinger():
    return {"MESSAGE": "Hi I am Pinging - Version 1"}

model_pickle = open("classifier.pkl","rb")
clf = pickle.load(model_pickle)


@app.route("/predict", methods = ["POST"])
def predict():
    loan_req = request.get_json()

    # Encoding the input according the model
    if loan_req["Gender"] == "Male":
        gender = 0
    else:
        gender = 1  
    if loan_req["Married"] == "No":
        married = 0
    else:
        married = 1
    
    # Encoding is not necessary for following variables
    applicant_income = loan_req["ApplicantIncome"]
    credit_history = loan_req["Credit_History"]
    loan_amount = loan_req["LoanAmount"]
    input_data = [[gender,married,applicant_income,loan_amount,credit_history]]
    prediction = clf.predict(input_data)
    # encoding is required for output predict also
    if prediction == 0:
        pred = "Rejected"
    else:
        pred = "Accepted"
    
    # returning the answer in json format
    return {"loan_approval_status":pred}
