from fastapi import FastAPI
from src.api.pydantic_models import InputData, PredictionResponse
import pandas as pd
import mlflow.sklearn

app = FastAPI()

# Load model from MLflow registry
model = mlflow.sklearn.load_model("models:/best_credit_model/Production")

@app.post("/predict", response_model=PredictionResponse)
def predict(data: InputData):
    # Convert the Pydantic model to a DataFrame
    input_df = pd.DataFrame([data.dict()])

    # Predict the probability of high credit risk
    proba = model.predict_proba(input_df)[0][1]  # Class 1 = high risk

    # Return the probability in the response
    return PredictionResponse(risk_score=proba)
