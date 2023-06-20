from offline_judge import OfflineJudge


def run_console_app():
    print("Offline Judge Console App")
    print("=========================")
    print()

    # Инстанцираме OJ-системата
    judge = OfflineJudge()

    # Питаме потребителят за 'пътя' на програмата и очаквания резултат
    program_path = input("Enter the program path: ")
    expected_result = input("Enter the expected result: ")

    # Задаваме програмния път за 'judge'
    judge.program_path = program_path

    # Стартираме тестовия случай
    result, message = judge.run_test_case(expected_result)

    # Принтираме резултата
    print(f"Result: {'Passed' if result else 'Failed'}")
    print(f"Message: {message}")


if __name__ == "__main__":
    run_console_app()
