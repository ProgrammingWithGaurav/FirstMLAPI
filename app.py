from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import json

app = FastAPI()


class model_input(BaseModel):
    Age: int
    Sex: int
    Cp: int
    Trestbps: int
    Chol: int
    Fbs: int
    Restecg: int
    Thalach: int
    Exang: int
    Oldpeak: float
    Slope: int
    Ca: int
    Thal: int


heart_disease_model = joblib.load('heart_disease_pred.joblib')


@app.post('/heart_disease_pred')
def diabetes_pred(input_parameters: model_input):
    input_data = input_parameters.json()
    # converting javascript json object to python dictionary
    input_dict = json.loads(input_data)

    age = input_dict['Age']
    sex = input_dict['Sex']
    cp = input_dict['Cp']
    trestbps = input_dict['Trestbps']
    chol = input_dict['Chol']
    fbs = input_dict['Fbs']
    restecg = input_dict['Restecg']
    thalach = input_dict['Thalach']
    exang = input_dict['Exang']
    oldpeak = input_dict['Oldpeak']
    slope = input_dict['Slope']
    ca = input_dict['Ca']
    thal = input_dict['Thal']

    input_list = [age, sex, cp, trestbps, chol, fbs,
                  restecg, thalach, exang, oldpeak, slope, ca, thal]
    pred = heart_disease_model.predict([input_list])
    
    if (pred[0] == 0):
        return "The person is not suffering from heart disease"
    else:
        return "The person may be suffering from herat disease"
