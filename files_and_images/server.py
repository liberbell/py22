import socket
from PIL import Image

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("localhost", 4571))
    s.listen(5)

    print('Server is up. Listening for connections....\n')

    client, address = s.accept()
    print("Connection to", address, "established\n")
    print("Client object:", client, "\n")

    # custom_file = open("server_files/meditations.txt", "rb")
    # custom_data = custom_file.read(40960)

    # while(custom_data):
    #     client.send(custom_data)
    #     custom_data = custom_file.read(40960)

    # print("Custom file successfully sent.")
    with open('server_files/dog.jpg', 'rb') as image_file:
        image_batch = image_file.read(40960)

        while (image_batch):
            client.send(image_batch)
            image_batch = image_file.read(40960)
            print("One batch sent to client...")

print("Image sent successfully.")
