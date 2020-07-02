import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    server_name = input("Enter your name: ")

    sock.bind(('localhost', 4571))