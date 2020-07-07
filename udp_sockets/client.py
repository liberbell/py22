import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM)as sock:
    sock.bind(("", 37020))

    while True:
        data, addr = sock.recvfrom(1024)
        print("Received message: ", data)