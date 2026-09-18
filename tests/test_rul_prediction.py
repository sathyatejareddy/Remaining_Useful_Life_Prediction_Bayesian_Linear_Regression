from pathlib import Path
import pandas as pd

RESULTS_FOLDER = Path("Data/Results")


def test_prediction_files():
    for experiment in ["FD001", "FD002"]:
        assert (
            RESULTS_FOLDER / f"predictions_{experiment}.csv"
        ).exists()


def test_prediction_data():
    for experiment in ["FD001", "FD002"]:
        data = pd.read_csv(
            RESULTS_FOLDER / f"predictions_{experiment}.csv"
        )

        assert "ID" in data.columns
        assert "Cycle" in data.columns
        assert "Predicted_RUL" in data.columns
        assert len(data) > 0
        assert data["Predicted_RUL"].notna().all()


def run_tests():
    print("\n[RUL Prediction Tests]")

    test_prediction_files()
    print("✓ Prediction files exist")

    test_prediction_data()
    print("✓ Prediction data is valid")

    print("✓ RUL prediction tests passed")


if __name__ == "__main__":
    run_tests()