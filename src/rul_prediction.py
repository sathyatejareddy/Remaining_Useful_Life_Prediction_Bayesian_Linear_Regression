import pandas as pd
from pathlib import Path
from sklearn.linear_model import BayesianRidge


PROCESSED_FOLDER = Path("Data/Processed")
RESULTS_FOLDER = Path("Data/Results")

RESULTS_FOLDER.mkdir(parents=True, exist_ok=True)


FEATURES = [
    "Setting1",
    "Setting2",
    "Setting3",
    "Sensor1",
    "Sensor2",
    "Sensor3",
    "Sensor4",
    "Sensor5",
    "Sensor6",
    "Sensor7",
    "Sensor8",
    "Sensor9",
    "Sensor10",
    "Sensor11",
    "Sensor12",
    "Sensor13",
    "Sensor14",
    "Sensor15",
    "Sensor16",
    "Sensor17",
    "Sensor18",
    "Sensor19",
    "Sensor20",
    "Sensor21"
]


def train_and_predict(experiment):
    train_file = PROCESSED_FOLDER / f"train_{experiment}.csv"
    test_file = PROCESSED_FOLDER / f"test_{experiment}.csv"
    output_file = RESULTS_FOLDER / f"predictions_{experiment}.csv"

    train_data = pd.read_csv(train_file)
    test_data = pd.read_csv(test_file)

    X_train = train_data[FEATURES]
    y_train = train_data["RUL"]

    X_test = test_data[FEATURES]

    model = BayesianRidge()

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    results = test_data[["ID", "Cycle"]].copy()
    results["Predicted_RUL"] = predictions

    results.to_csv(output_file, index=False)

    print(f"\n{experiment} prediction completed.")
    print(f"Predictions saved to: {output_file}")


if __name__ == "__main__":
    for experiment in ["FD001", "FD002"]:
        train_and_predict(experiment)

    print("\nAll RUL(Remaining USeful Fuel) predictions completed.")