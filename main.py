from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
import uvicorn

# Initialize the FastAPI app
app = FastAPI()

# Global variable to hold the model pipeline
nlp_pipeline = None

# Load the model during application startup
@app.on_event("startup")
def load_model():
    global nlp_pipeline
    try:
        # Load the BERT model for a specific task, e.g., sentiment-analysis
        nlp_pipeline = pipeline("sentiment-analysis")
        print("Model loaded successfully!")
    except Exception as e:
        print(f"Error loading model: {e}")
        raise e

# Define the input schema
class InputText(BaseModel):
    text: str

# Define the output schema
class OutputPrediction(BaseModel):
    label: str
    score: float

# API endpoint for predictions
@app.post("/predict", response_model=OutputPrediction)
def predict(input_text: InputText):
    try:
        # Use the loaded pipeline to make a prediction
        prediction = nlp_pipeline(input_text.text)
        result = prediction[0]  # The pipeline returns a list of results
        return OutputPrediction(label=result["label"], score=result["score"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

@app.post("/predict-on-demand", response_model=OutputPrediction)
def predict_on_demand(input_text: InputText):
    try:
        # Load the model pipeline for every request
        nlp_pipeline = pipeline("sentiment-analysis")
        prediction = nlp_pipeline(input_text.text)
        result = prediction[0]
        return OutputPrediction(label=result["label"], score=result["score"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

# Main entry point for running the server
if __name__ == "__main__":
    # Run the server on host 0.0.0.0 and port 8001
    uvicorn.run(app, host="0.0.0.0", port=8001)
