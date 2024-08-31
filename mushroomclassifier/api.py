from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conlist
import joblib
import numpy as np

app = FastAPI()

loaded_model = joblib.load('model.pkl')

class feature(BaseModel):
    features: conlist(float, min_length = 23, max_length = 23)


@app.post('/predict')
def predict(data:feature):
    try:
        features = np.array(data.features).reshape(1, -1)
        prediction = loaded_model.predict(features)
        return (f'Prediction : {int(prediction)}')
    except Exception as e:
        return HTTPException(status_code = 500, detail=str(e))
