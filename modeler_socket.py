from queue import Queue
import time
import socket

data_queue = Queue()


def handle_client(client_socket):
    request = client_socket.recv(1024)
    data = request.decode("utf-8")
    perform_inference(data)
    client_socket.close()

def perform_inference(data):
    # 这里是你的推理逻辑，根据需要进行修改
    print(f"Received data: {data}")
    # 进行推理操作
    result = "Inference result"
    print(f"Inference result: {result}")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 8888))
    server_socket.listen(5)
    print("Modeler server started, listening on port 8888")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address[0]}:{client_address[1]}")
        handle_client(client_socket)

if __name__ == "__main__":
    start_server()