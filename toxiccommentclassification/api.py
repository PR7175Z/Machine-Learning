from fastapi import FastAPI, HTTPException
import joblib
from pydantic import BaseModel, conlist
from fastapi.middleware.cors import CORSMiddleware
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

model = joblib.load('models/toxiccommentclaasifier.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

class feature(BaseModel):
    features:str

@app.post('/predict')
def predict(inputdata: feature):
    try:
        inputdatavect = vectorizer(inputdata.feature)
        prediction = model.predict(inputdatavect)
        return prediction
    except Exception as e:
        return HTTPException(status_code = 500, detail = str(e))