import socket
import os

HOST = "127.0.0.1"
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

username = input("Username: ")
password = input("Password: ")

client_socket.send(username.encode())
client_socket.send(password.encode())

response = client_socket.recv(1024).decode()
if response != "AUTH_OK":
    print("Authentication failed")
    client_socket.close()
    exit()

filepath = input("Enter file path to send: ")

if not os.path.exists(filepath):
    print("File not found")
    client_socket.close()
    exit()

filename = os.path.basename(filepath)
filesize = os.path.getsize(filepath)

client_socket.send(filename.encode())
client_socket.send(str(filesize).encode())

with open(filepath, "rb") as f:
    while True:
        chunk = f.read(1024)
        if not chunk:
            break
        client_socket.send(chunk)

client_socket.close()
print("File sent successfully")
