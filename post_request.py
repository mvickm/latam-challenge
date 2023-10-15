import logging
import requests

# Configure the logging
logging.basicConfig(level=logging.INFO)  # Set the desired logging level

# URL
url = 'https://advana-challenge-check-api-cr-k4hdbggvoq-uc.a.run.app/data-engineer'

# Data to POST as dict
data = {
    'name': 'María Victoria Munafó',
    'mail': 'mariavictoriamunafo@gmail.com',
    'github_url': 'https://github.com/mvickm/latam-challenge.git'
}

# POST request
response = requests.post(url, json=data)

# Check if the request was successful (response code 200)
if response.status_code == 200:
    logging.info('Successful POST request')
    logging.info('Server response:')
    logging.info(response.text)  # Display the server response
else:
    logging.error('Error in the POST request. Response code: %d', response.status_code)
