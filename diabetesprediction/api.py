from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conlist
import pickle

app = FastAPI()

with open('diabetes_prediction.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

class feature(BaseModel):
    features:conlist(float, min_length = 10, max_length = 10)

@app.post('/predict')
def predict(data: feature):
    try:
        prediction = loaded_model.predict([data.features])
        return (f'Prediction : {int(prediction)}')
    except Exception as e:
        return HTTPException(status_code = 500, detail = str(e))