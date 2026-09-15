import joblib

from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score


MODEL_PATH = "models/model.pkl"

data = load_iris()

model = joblib.load(MODEL_PATH)

predictions = model.predict(data.data)

accuracy = accuracy_score(
    data.target,
    predictions
)

print(f"Model Accuracy: {accuracy:.4f}")

MIN_ACCURACY = 0.90

if accuracy < MIN_ACCURACY:

    print(
        f"MODEL VALIDATION FAILED: "
        f"{accuracy:.4f} < {MIN_ACCURACY}"
    )

    raise SystemExit(1)

print("MODEL VALIDATION PASSED")
