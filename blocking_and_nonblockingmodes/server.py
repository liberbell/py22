import socket
from datetime import datetime

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("localhost", 4571))
    s.listen(5)

    print("Server is up. Listening for connections...")

    client, address = s.accept()
    print("Connection to: ", address, "established.\n")
    print("Client object: ", client, "\n")