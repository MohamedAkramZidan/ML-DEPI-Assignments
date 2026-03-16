from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from preprocessing import preprocess_texts

# Load model & vectorizer
model = joblib.load("xgboost_model.joblib")
vectorizer = joblib.load("tfidf_vectorizer.joblib")

app = FastAPI(title="Spam Detector API")

class TextRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Spam Detector API is running!"}

@app.post("/predict")
def predict(request: TextRequest):
    try:
        # Preprocess input
        processed = preprocess_texts([request.text])  # returns list of strings
        X_vec = vectorizer.transform(processed)       # TF-IDF transform
        prediction = model.predict(X_vec)[0]         # model predict
        return {"prediction": int(prediction)}
    except Exception as e:
        return {"error": str(e)}  # return the error instead of crashing