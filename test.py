import json
import requests

url = 'http://127.0.0.1:8000/heart_disease_pred'

input_data = {
    'Age': 52,
    'Sex': 1,
    'Cp': 0,
    'Trestbps': 125,
    'Chol': 212,
    'Fbs': 0,
    'Restecg': 1,
    'Thalach': 168,
    'Exang': 0,
    'Oldpeak': 1.0,
    'Slope': 2,
    'Ca': 2,
    'Thal': 3
}

# converting to json
input_json = json.dumps(input_data)
res = requests.post(url, data=input_json)
print(res.text)
