import socket
import os
import logging
import threading
from crypto_utils import encrypt_data

HOST = "127.0.0.1"
PORT = 5000

# ---------- Logging ----------
logging.basicConfig(
    filename="server.log",
    level=logging.INFO,
    format="%(asctime)s | %(message)s"
)

# ---------- Load users ----------
def load_users():
    users = {}
    with open("users.txt", "r") as f:
        for line in f:
            line = line.strip()
            if ":" in line:
                u, p = line.split(":")
                users[u] = p
    return users

users = load_users()

# ---------- Client handler ----------
def handle_client(conn, addr):
    username = "-"
    try:
        print("Connected by", addr)

        # --- AUTH ---
        username = conn.recv(1024).decode().strip()
        password = conn.recv(1024).decode().strip()

        if username not in users or users[username] != password:
            conn.send(b"AUTH_FAIL")
            logging.info(f"user={username} | file=- | status=AUTH_FAIL")
            return

        conn.send(b"AUTH_OK")

        # --- FILE INFO ---
        filename = conn.recv(1024).decode().strip()
        filesize = int(conn.recv(1024).decode().strip())

        os.makedirs("received_files", exist_ok=True)
        filepath = os.path.join("received_files", filename)

        # --- RECEIVE FILE ---
        file_data = b""
        received = 0
        while received < filesize:
            chunk = conn.recv(1024)
            if not chunk:
                break
            file_data += chunk
            received += len(chunk)

        # --- ENCRYPT & SAVE ---
        encrypted_data = encrypt_data(file_data)
        with open(filepath, "wb") as f:
            f.write(encrypted_data)

        logging.info(f"user={username} | file={filename} | status=SUCCESS")
        print(f"{addr} | {filename} received")

    except Exception as e:
        logging.error(f"user={username} | error={str(e)}")
        print("Error handling client", addr, e)

    finally:
        conn.close()

# ---------- Main server ----------
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Server listening on port {PORT}")

    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(
            target=handle_client,
            args=(conn, addr),
            daemon=True
        )
        thread.start()

if __name__ == "__main__":
    main()
