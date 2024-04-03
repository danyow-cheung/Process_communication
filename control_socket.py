from flask import Flask, request, jsonify
from queue import Queue
import socket
app = Flask(__name__)
data_queue = Queue()

def send_data_to_modeler(data):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 8888))
    client_socket.send(data.encode("utf-8"))
    client_socket.close()

@app.route("/", methods=["POST"])
def receive_data():
    data = request.json.get("data")
    data_queue.put(data)
    return jsonify({"message": "Data received"})

if __name__ == "__main__":
    app.run(host="192.168.0.37", port=5000)