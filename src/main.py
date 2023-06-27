import asyncio
import websockets
import subprocess
import json

class OfflineJudge:
    def __init__(self):
        self.program_source = None

    def run_test_case(self, expected_result):
        try:
            with open("temp_program.py", "w") as file:
                file.write(self.program_source)


            process = subprocess.Popen(
                ["python", "temp_program.py"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                universal_newlines=True
            )
            output, error = process.communicate(timeout=5)  # Timeout set to 5 seconds


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

async def start_websocket_server(websocket, path):
    offline_judge = OfflineJudge()

    async for message in websocket:
        data = json.loads(message)
        program_source = data.get('source')
        expected_result = data.get('expected')

        offline_judge.program_source = program_source
        result, message = offline_judge.run_test_case(expected_result)

        response = {
            "result": result,
            "message": message
        }

        await websocket.send(json.dumps(response))

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(
        websockets.serve(start_websocket_server, "localhost", 8765)
    )
    asyncio.get_event_loop().run_forever()

