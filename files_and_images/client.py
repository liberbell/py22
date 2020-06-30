import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as r:
    r.connect(("localhost", 4571))
    custom_file = open("client_files/recieved_file.txt", "wb")