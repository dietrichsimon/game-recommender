'''test file for the flask app'''

from app.py import app
import pytest
import requests

def test_response_status():
    response = requests.get('http://127.0.0.1:5000/')
    assert response.status_code == 200
