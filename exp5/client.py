import socket
import threading


def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                print("\nDisconnected from server.")
                break

            print(f"\n{message}")

        except OSError:
            break


def chat_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect(("localhost", 55555))
        print("Connected to chat server.")
        print("Type a message and press Enter. Type 'exit' to leave.")

    except OSError as error:
        print(f"Unable to connect: {error}")
        client_socket.close()
        return

    receive_thread = threading.Thread(
        target=receive_messages,
        args=(client_socket,),
        daemon=True,
    )
    receive_thread.start()

    try:
        while True:
            message = input()
            if message.lower() == "exit":
                break

            client_socket.sendall(message.encode())

    except (EOFError, KeyboardInterrupt, OSError):
        pass

    finally:
        client_socket.close()
        print("Disconnected from chat server.")


if __name__ == "__main__":
    chat_client()
