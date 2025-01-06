import requests
from requests.auth import HTTPBasicAuth

jenkins_url = 'http://jenkins.local:8080/job/my-job/build'
username = 'admin'
api_token = 'your_api_token'

response = requests.post(jenkins_url, auth=HTTPBasicAuth(username, api_token))

if response.status_code == 201:
    print("Jenkins job triggered successfully!")
else:
    print(f"Error: {response.status_code}")