I'd like to show you my project - it's online judge system written in Python. It evaluates and tests code submissions. There is one WebSocket Server which listens to incoming Websocket connections on "ws://localhost:8765". I have an OfflineJudge class that handles the actual evaluation of code submissions. It has a method called run_test_case that takes a code snippet and an expected result as input and returns whether the code snippet produces the expected result. hen a client connects to the WebSocket server, it can send a JSON message to the server. The JSON message typically contains the source code to be evaluated and the expected result. The server receives the JSON message, extracts the code source and expected result, and passes them to the OfflineJudge class's run_test_case method. The OfflineJudge class then executes the code in a controlled environment (sandbox), captures the output, and compares it to the expected result.