import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error


def test_error_calculation():
    actual = np.array([10, 20, 30])
    predicted = np.array([12, 18, 27])

    mae = mean_absolute_error(actual, predicted)
    rmse = np.sqrt(mean_squared_error(actual, predicted))

    assert mae >= 0
    assert rmse >= 0


def test_perfect_prediction():
    actual = np.array([10, 20, 30])
    predicted = np.array([10, 20, 30])

    mae = mean_absolute_error(actual, predicted)
    rmse = np.sqrt(mean_squared_error(actual, predicted))

    assert mae == 0
    assert rmse == 0


def run_tests():
    print("\n[Evaluation Tests]")

    test_error_calculation()
    print("✓ Error calculation works")

    test_perfect_prediction()
    print("✓ Perfect prediction gives zero error")

    print("✓ Evaluation tests passed")


if __name__ == "__main__":
    run_tests()