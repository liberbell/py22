import socket
from datetime import datetime

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("localhost", 4571))
    s.listen(5)