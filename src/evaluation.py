import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.metrics import mean_absolute_error, mean_squared_error

RESULTS_FOLDER = Path("Data/Results")
RAW_FOLDER = Path("Data/Raw")


def evaluate(experiment):
    predictions = pd.read_csv(
        RESULTS_FOLDER / f"predictions_{experiment}.csv"
    )

    predictions = (
        predictions
        .sort_values(["ID", "Cycle"])
        .groupby("ID")
        .tail(1)
        .sort_values("ID")
    )

    actual = pd.read_csv(
        RAW_FOLDER / f"RUL_{experiment}.txt",
        sep=r"\s+",
        header=None,
        names=["Actual_RUL"]
    )

    y_pred = predictions["Predicted_RUL"].values
    y_true = actual["Actual_RUL"].values

    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))

    print(f"{experiment}: MAE = {mae:.2f}, RMSE = {rmse:.2f}")


if __name__ == "__main__":
    evaluate("FD001")
    evaluate("FD002")