import joblib

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(
    title="Iris Classification API",
    version="1.0.0"
)


MODEL_PATH = "models/model.pkl"


try:

    model = joblib.load(MODEL_PATH)

except Exception as e:

    model = None

    print(f"Model loading failed: {e}")


class IrisInput(BaseModel):

    features: list[float]


@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "version": "1.0.0"
    }


@app.post("/predict")
def predict(input_data: IrisInput):

    if len(input_data.features) != 4:

        raise HTTPException(
            status_code=400,
            detail="Exactly 4 features required."
        )

    if model is None:

        raise HTTPException(
            status_code=503,
            detail="Model is not available."
        )

    prediction = model.predict(
        [input_data.features]
    )

    return {
        "model_version": "1.0.0",
        "prediction": int(prediction[0])
    }
