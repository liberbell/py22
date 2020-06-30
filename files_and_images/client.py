import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as r:
    r.connect(("localhost", 4571))