import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    client_name = input("Enter your name: ")

    sock.connect(("localhost", 4571))
    sock.send(client_name.encode())