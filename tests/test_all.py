from test_data_processing import run_tests as test_data_processing
from test_rul_prediction import run_tests as test_rul_prediction
from test_evaluation import run_tests as test_evaluation


def main():
    print("========================================")
    print("           PROJECT TESTING")
    print("========================================")

    try:
        test_data_processing()
        test_rul_prediction()
        test_evaluation()

        print("\n========================================")
        print("    ALL TESTS PASSED SUCCESSFULLY")
        print("========================================")

    except Exception as error:
        print("\n========================================")
        print("           TEST FAILED")
        print("========================================")
        print(f"Error: {error}")


if __name__ == "__main__":
    main()