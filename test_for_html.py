from predictions_with_html import app
import pytest

# Setup a fixture to create the test client for the Flask app
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test the home page, ensuring the loan form is present in the HTML
def test_home_page(client):
    """Test that the home page loads and the form is present."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Loan Application Form' in response.data  # Check that the form is rendered

# Test the ping endpoint to ensure it returns the correct JSON response
def test_pinger(client):
    """Test the ping endpoint for correct response."""
    response = client.get('/ping')
    assert response.status_code == 200
    assert response.json == {"MESSAGE": "Hi I am Pinging - Version 1"}

# Test the predict endpoint by sending form data and checking the HTML response
def test_predictions(client):
    """Test the predict endpoint with form data."""
    # Simulate form data as a dictionary (the same structure as in HTML form)
    test_data = {
        'Gender': 'Male',
        'Married': 'Yes',
        'ApplicantIncome': '50000',  # Values should be strings as form data
        'LoanAmount': '5000',
        'Credit_History': '1'
    }

    # Post the data to the /predict endpoint
    response = client.post('/predict', data=test_data)
    
    # Check that the response is 200 OK
    assert response.status_code == 200

    # Check that the response contains the text for the loan approval result
    assert b'Loan Application Status: Accepted' in response.data
