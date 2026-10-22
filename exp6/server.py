import socket


def file_transfer_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_socket.bind(("localhost", 12345))

    # Listen for incoming connections
    server_socket.listen(1)
    print("Server listening on port 12345...")

    # Accept a connection from a client
    connection, client_address = server_socket.accept()
    print(f"Connected by {client_address}")

    # Receive the file name
    filename = connection.recv(1024).decode()
    print(f"Receiving file: {filename}")

    with open(f"received_{filename}", "wb") as file:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            file.write(data)

    print(f"File received and saved as received_{filename}")

    connection.close()
    server_socket.close()


if __name__ == "__main__":
    file_transfer_server()
