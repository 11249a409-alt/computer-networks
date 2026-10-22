import socket

# Get the hostname of the machine
hostname = socket.gethostname()

# Get the IP address associated with the hostname
ip_address = socket.gethostbyname(hostname)

# Display the results
print("Hostname:", hostname)
print("IP Address:", ip_address)
