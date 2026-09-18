import pandas as pd
from pathlib import Path
from sklearn.linear_model import BayesianRidge


PROCESSED_FOLDER = Path("Data/Processed")


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


def train_model(experiment):
    data = pd.read_csv(
        PROCESSED_FOLDER / f"train_{experiment}.csv"
    )

    X = data[FEATURES]
    y = data["RUL"]

    model = BayesianRidge()
    model.fit(X, y)

    return model


def manual_input():
    values = {}

    print("\nEnter the values for the following parameters:")

    for feature in FEATURES:
        while True:
            try:
                values[feature] = float(input(f"{feature}: "))
                break
            except ValueError:
                print("Please enter a number.")

    return pd.DataFrame([values])


def dataset_input(experiment):
    data = pd.read_csv(
        PROCESSED_FOLDER / f"train_{experiment}.csv"
    )

    print("\nAvailable Engine IDs:")
    print(data["ID"].unique())

    while True:
        try:
            engine_id = int(input("\nEnter Engine ID: "))

            engine_data = data[data["ID"] == engine_id]

            if engine_data.empty:
                print("Engine ID not found.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    print("\nAvailable cycles for this engine:")
    print(
        engine_data["Cycle"].min(),
        "to",
        engine_data["Cycle"].max()
    )

    while True:
        try:
            cycle = int(input("Enter Cycle: "))

            selected = engine_data[
                engine_data["Cycle"] == cycle
            ]

            if selected.empty:
                print("Cycle not found for this engine.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    input_data = selected[FEATURES]

    actual_rul = selected["RUL"].iloc[0]

    return input_data, actual_rul, engine_id, cycle


def main():

    print("========================================")
    print("       RUL PREDICTION APPLICATION")
    print("========================================")

    print("\nSelect dataset:")
    print("1. FD001")
    print("2. FD002")

    choice = input("\nEnter choice: ")

    if choice == "1":
        experiment = "FD001"
        print("\nFD001 selected.")
        print("Operating conditions: 1")

    elif choice == "2":
        experiment = "FD002"
        print("\nFD002 selected.")
        print("Operating conditions: 6")

    else:
        print("\nInvalid choice.")
        return

    print("\nTraining Bayesian Linear Regression model...")

    model = train_model(experiment)

    print("Model trained successfully.")

    print("\nChoose input method:")
    print("1. Enter parameters manually")
    print("2. Use an existing engine from the dataset")

    input_choice = input("\nEnter choice: ")

    if input_choice == "1":

        input_data = manual_input()

        prediction = model.predict(input_data)[0]

        print("\n========================================")
        print("           PREDICTION RESULT")
        print("========================================")
        print(f"Dataset: {experiment}")
        print(f"Predicted RUL: {prediction:.2f} cycles")
        print("========================================")

    elif input_choice == "2":

        result = dataset_input(experiment)

        input_data = result[0]
        actual_rul = result[1]
        engine_id = result[2]
        cycle = result[3]

        prediction = model.predict(input_data)[0]

        print("\n========================================")
        print("           PREDICTION RESULT")
        print("========================================")
        print(f"Dataset: {experiment}")
        print(f"Engine ID: {engine_id}")
        print(f"Cycle: {cycle}")
        print(f"Actual RUL: {actual_rul:.2f} cycles")
        print(f"Predicted RUL: {prediction:.2f} cycles")
        print("========================================")

    else:
        print("\nInvalid choice.")


if __name__ == "__main__":
    main()