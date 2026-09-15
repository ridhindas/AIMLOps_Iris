import os
import joblib

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "model.pkl")


def retrain_model():

    print("Loading Iris dataset...")

    data = load_iris()

    print("Training Random Forest model...")

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(data.data, data.target)

    os.makedirs(MODEL_DIR, exist_ok=True)

    joblib.dump(model, MODEL_PATH)

    print(f"Model saved: {MODEL_PATH}")


if __name__ == "__main__":
    retrain_model()
