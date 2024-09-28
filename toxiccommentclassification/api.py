from fastapi import FastAPI, HTTPException
import joblib
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

model = joblib.load('models/toxiccommentclassifier.pkl')

@app.post('/predict')
def predict():
    try:
        return 'Hello'
    except Exception as e:
        return HTTPException(status_code = 500, detail = str(e))