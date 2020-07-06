import time
import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.connect(0.2)
    sock.bind(("localhost", 4571))

    i = 1

    while True:
        message = bytes("Message #" + str(i), "UTF-8")
        sock.sendto(message, ("localhost", 37020))