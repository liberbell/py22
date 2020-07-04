import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(("localhost", 4571))
    sock.setblocking(Ture)

    data = bytes("Hello Server\n", "UTF-8") * 1024 * 1024 * 10
    print("Size of data sent: %1 bytes." %len(data))