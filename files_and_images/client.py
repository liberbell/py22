import socket
from PIL import Image

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as r:
    r.connect(("localhost", 4571))
    # custom_file = open("client_files/received_file.txt", "wb")
    with open('client_files/received_file.jpg', 'wb') as image_file:
        while True:
            data = r.recv(40960)
            if not data:
                print("No messages from the server. Closing the connection....")
                break
            
            image_file.write(data)
            print("Batch of data written to file....")
            
        image_file.close()