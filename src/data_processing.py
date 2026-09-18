import pandas as pd
from pathlib import Path

RAW_FOLDER = Path("Data/Raw")
PROCESSED_FOLDER = Path("Data/Processed")
PROCESSED_FOLDER.mkdir(parents=True, exist_ok=True)

columns = [
    "ID",
    "Cycle",
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


def process_training_file(experiment):
    input_file = RAW_FOLDER / f"train_{experiment}.txt"
    output_file = PROCESSED_FOLDER / f"train_{experiment}.csv"

    data = pd.read_csv(
        input_file,
        sep=r"\s+",
        header=None,
        names=columns
    )

    max_cycle = data.groupby("ID")["Cycle"].transform("max")
    data["RUL"] = max_cycle - data["Cycle"]

    data.to_csv(output_file, index=False)

    print(f"Processed {experiment}")
    print(f"Saved to: {output_file}")


def process_test_file(experiment):
    input_file = RAW_FOLDER / f"test_{experiment}.txt"
    output_file = PROCESSED_FOLDER / f"test_{experiment}.csv"

    data = pd.read_csv(input_file,sep=r"\s+",header=None,names=columns)
    data.to_csv(output_file, index=False)

    print(f"Processed {experiment} test data")
    print(f"Saved to: {output_file}")


if __name__ == "__main__":
    for experiment in ["FD001", "FD002"]:
        process_training_file(experiment)
        process_test_file(experiment)

    print("\nAll data processing completed.")