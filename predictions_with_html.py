import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")  # Home page URL
def home():
    return render_template("loan_form.html")  # Render HTML form

@app.route("/ping", methods=["GET"])  # Home page/ping
def pinger():
    return {"MESSAGE": "Hi I am Pinging - Version 1"}

# Load model
model_pickle = open("classifier.pkl", "rb")
clf = pickle.load(model_pickle)

@app.route("/predict", methods=["POST"])
def predict():
    # Get data from the form
    loan_req = request.form

    # Encoding the input according to the model
    gender = 0 if loan_req["Gender"] == "Male" else 1
    married = 0 if loan_req["Married"] == "No" else 1
    applicant_income = int(loan_req["ApplicantIncome"])
    loan_amount = int(loan_req["LoanAmount"])
    credit_history = int(loan_req["Credit_History"])

    # Prepare input data for the model
    input_data = [[gender, married, applicant_income, loan_amount, credit_history]]
    
    # Make a prediction
    prediction = clf.predict(input_data)
    
    # Encoding prediction result
    pred = "Rejected" if prediction == 0 else "Accepted"
    
    # Return result to the webpage
    return render_template("loan_form.html", prediction_result=pred)

if __name__ == "__main__":
    app.run(debug=True)