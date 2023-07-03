import asyncio
import websockets
import subprocess
import json

class OfflineJudge:
  def __init__(self):
    self.program_source = None

  def run_test_case(self, expected_result):
    response = {
      result: False,
      expected = expected_result
    }

    # add data for memory/cpu consuption, execution time
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
        response.strerr = "Runtime error"
        response.error = error
        return response

      output = output.strip()
      response.output = output
      if output == str(expected_result):
        response.result = True

    except subprocess.TimeoutExpired:
      response.strerr = "Time Limit Exceeded"

    except Exception as e:
      response.error = str(e)

    # delete temp file temp_program.py
    return response

async def start_websocket_server(websocket, path):
  offline_judge = OfflineJudge()

  async for message in websocket:
    data = json.loads(message)
    exec_type = data.get('type')
    program_source = data.get('source')
    expected_result = data.get('expected')

    if exec_type == 'source':
      offline_judge.program_source = program_source
      response = offline_judge.run_test_case(expected_result)
    elif exec_type == 'file':
      # write for file logic + upload to server

    await websocket.send(json.dumps(response))

if __name__ == "__main__":
  asyncio.get_event_loop().run_until_complete(
    websockets.serve(start_websocket_server, "localhost", 8765)
  )
  asyncio.get_event_loop().run_forever()

