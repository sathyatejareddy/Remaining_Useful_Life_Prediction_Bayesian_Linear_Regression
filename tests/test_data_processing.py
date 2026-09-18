from pathlib import Path
import pandas as pd

PROCESSED_FOLDER = Path("Data/Processed")


def test_processed_files():
    for experiment in ["FD001", "FD002"]:
        assert (PROCESSED_FOLDER / f"train_{experiment}.csv").exists()
        assert (PROCESSED_FOLDER / f"test_{experiment}.csv").exists()


def test_training_rul():
    for experiment in ["FD001", "FD002"]:
        data = pd.read_csv(PROCESSED_FOLDER / f"train_{experiment}.csv")

        assert "RUL" in data.columns
        assert data["RUL"].notna().all()
        assert (data["RUL"] >= 0).all()


def run_tests():
    print("\n[Data Processing Tests]")

    test_processed_files()
    print("✓ Processed files exist")

    test_training_rul()
    print("✓ Training RUL values are valid")

    print("✓ Data processing tests passed")


if __name__ == "__main__":
    run_tests()