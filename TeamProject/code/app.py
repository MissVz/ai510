from flask import Flask, request, render_template, jsonify
import urllib.request
import json
import os
import ssl
import locale

# Create a Flask application instance
app = Flask(__name__)

# Function to allow self-signed HTTPS certificates
def allowSelfSignedHttps(allowed):
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

# Allow self-signed HTTPS certificates
allowSelfSignedHttps(True)

# Set locale for currency formatting
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')  # Render the home page

# Define the predict route to handle POST requests
@app.route('/predict', methods=['POST'])
def predict():
    # Collect data from the form and prepare it for the API request
    data = {
        "Inputs": {
            "data": [
                {
                    "bathrooms": float(request.form['bathrooms']),
                    "sqft_living": float(request.form['sqft_living']),
                    "sqft_lot": float(request.form['sqft_lot']),
                    "waterfront": int(request.form['waterfront']),
                    "view": int(request.form['view']),
                    "condition": int(request.form['condition']),
                    "grade": int(request.form['grade']),
                    "sqft_above": float(request.form['sqft_above']),
                    "sqft_basement": float(request.form['sqft_basement']),
                    "yr_built": int(request.form['yr_built']),
                    "yr_renovated": int(request.form['yr_renovated']),
                    "zipcode": int(request.form['zipcode']),
                    "lat": float(request.form['lat']),
                    "long": float(request.form['long']),
                    "sqft_living15": float(request.form['sqft_living15']),
                    "sqft_lot15": float(request.form['sqft_lot15'])
                }
            ]
        }
    }

    # Convert the data to a JSON string
    body = str.encode(json.dumps(data))
    # URL of the API endpoint
    url = 'http://3a271271-181e-422a-9847-52137b72e7c5.westus3.azurecontainer.io/score'
    # API key for authentication
    api_key = 'J0QTCd3P4ePk0bf5xV0FAbqLeODihzC5'
    # Headers for the API request
    headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}

    # Create a request object
    req = urllib.request.Request(url, body, headers)

    try:
        # Send the request and get the response
        response = urllib.request.urlopen(req)
        # Parse the JSON response
        result = json.loads(response.read())
        # Extract the prediction value
        prediction_value = result["Results"][0]
        # Format the prediction value as currency
        formatted_result = locale.currency(prediction_value, grouping=True)
        # Render the result page with the formatted prediction
        return render_template('result.html', result=formatted_result)
    except urllib.error.HTTPError as error:
        # Handle HTTP errors
        return jsonify({"error": str(error)})

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)