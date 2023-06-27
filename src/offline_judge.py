import subprocess


class OfflineJudge:
    def __init__(self):
        self.program_path = None

    def run_test_case(self, expected_result):
        try:
            process = subprocess.Popen(
                ["python", self.program_path],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                universal_newlines=True
            )
            output, error = process.communicate(timeout=5)


            if process.returncode != 0:
                return False, f"Runtime Error:\n{error}"

            output = output.strip()
            if output == str(expected_result):
                return True, "Correct Answer"
            else:
                return False, f"Wrong Answer:\nExpected Result: {expected_result}\nActual Result: {output}"

        except subprocess.TimeoutExpired:
            return False, "Time Limit Exceeded"

        except Exception as e:
            return False, f"Error occurred: {str(e)}"
