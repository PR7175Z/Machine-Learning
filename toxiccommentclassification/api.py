from fastapi import FastAPI, HTTPException
import joblib
from pydantic import BaseModel, conlist
from fastapi.middleware.cors import CORSMiddleware
from sklearn.feature_extraction.text import CountVectorizer
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
vectorize = joblib.load('models/vectorizer.pkl')

class InputData(BaseModel):
    comment: str

@app.post('/predict')
def predict(inputdata: InputData):
    try:
        cmt = [inputdata.comment]
        print(cmt)
        inputdatavect = vectorize.transform(cmt)
        prediction = model.predict(inputdatavect)
        return {"pred": int(prediction)}
    except Exception as e:
        return HTTPException(status_code = 500, detail = str(e))