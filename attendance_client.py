import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 7777

# Connect to the server on local computer
s.connect(('127.0.0.1', port))

# Define the name and ID
name = 'student'
ID = '1234'

# Data to send
data = name + ',' + ID

# Convert the string to binary values
data = data.encode()

# Send the name and ID
s.sendall(data)

# receive the confirmation from the server and decoding to get the string.
print (s.recv(1024).decode())

# close the connection
s.close()