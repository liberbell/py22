import socket
from datetime import datetime

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("localhost", 4571))
    s.listen(5)

    print("Server is up. Listening for connections...\n")

    client, address = s.accept()
    print("Connection to: ", address, "established.\n")
    print("Client object: ", client, "\n")

    start_time = datetime.now()
    data = client.recv(1024)
    total_received_size = len(data)

    i = 1
    while data:
        print(data.decode("UTF-8"))
        data = client.recv(1024)
        total_received_size += len(data)
        i += 1