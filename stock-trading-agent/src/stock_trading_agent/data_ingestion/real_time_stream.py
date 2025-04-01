# from websocket import create_connection
# import json
# import logging
# import time

# class RealTimeStream:
#     def __init__(self, url, on_message):
#         self.url = url
#         self.on_message = on_message
#         self.ws = None
#         self.keep_running = True

#     def connect(self):
#         try:
#             self.ws = create_connection(self.url)
#             logging.info("Connected to WebSocket")
#         except Exception as e:
#             logging.error(f"Failed to connect to WebSocket: {e}")
#             self.keep_running = False

#     def listen(self):
#         while self.keep_running:
#             try:
#                 message = self.ws.recv()
#                 self.on_message(json.loads(message))
#             except Exception as e:
#                 logging.error(f"Error receiving message: {e}")
#                 self.keep_running = False

#     def close(self):
#         if self.ws:
#             self.ws.close()
#             logging.info("WebSocket connection closed")

#     def run(self):
#         self.connect()
#         if self.keep_running:
#             self.listen()
#         self.close()

# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO)

#     def handle_message(message):
#         logging.info(f"Received message: {message}")

#     url = "wss://your.websocket.url"  # Replace with your WebSocket URL
#     stream = RealTimeStream(url, handle_message)
#     stream.run()