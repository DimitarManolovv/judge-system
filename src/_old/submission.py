import websocket
import json

def submit_case():
  source_code = input("Enter source code: ")
  expected_result = input("Enter expected result: ")

  uri = "ws://localhost:8765"
  ws = websocket.WebSocket()
  ws.connect(uri)
  data = {
    "source_code": source_code,
    "expected_result": expected_result
  }
  ws.send(json.dumps(data))
  response = ws.recv()
  result_message = json.loads(response)
  result = result_message["result"]
  memory = result_message["memory"]
  error = result_message["error"]
  print(f"Result: {result}")
  print(f"Memory Used: {memory} bytes")
  if error:
    print(f"Error: {error}")
  ws.close()

if __name__ == "__main__":
  submit_case()

