import socket

# Create a TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8080))
server.listen(1)
print("HTTP Server running on http://localhost:8080 ...")

while True:
    conn, addr = server.accept()
    request = conn.recv(1024).decode()
    print("--- Received HTTP Request ---")
    print(request)

    # Build a valid HTTP response string
    http_response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        "Connection: close\r\n"
        "\r\n"
        "<html><body><h1>welcome to Computer networks Lab!</h1></body></html>"
    )

    # Send the HTTP response and close
    conn.sendall(http_response.encode())
    conn.close()
