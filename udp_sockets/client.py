import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM)as sock:
    sock.bind("", 37020)