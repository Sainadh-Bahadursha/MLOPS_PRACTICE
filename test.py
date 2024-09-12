from predictions import app
import pytest
import json

# this act like a server. We will call this when we want to call the server
@pytest.fixture
def client(): 
    with app.test_client() as client:
        yield client

# test home page
def test_hello_world(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json == "<p>Hello, World! - Version 1</p>"

# should check the response code is 200 - successful or not
# should check output of pinger - "I am pinging"
def test_pinger(client):
    resp = client.get("/ping")
    assert resp.status_code == 200
    assert resp.json == {"MESSAGE": "Hi I am Pinging - Version 1"}

def test_predictions(client):
    test_data = {
    "Gender": "Male",
    "Married": "Yes",
    "ApplicantIncome": 500000,
    "LoanAmount": 5000,
    "Credit_History": 1.0 
    }
    resp = client.post("/predict",json = test_data)
    assert resp.status_code == 200
    assert resp.json == {"loan_approval_status":"Rejected"}