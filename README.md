# Secure File Transfer System (Python)

## Overview
This project is a secure, TCP-based client–server file transfer system implemented in Python.  
It allows authenticated clients to upload files to a server, where files are encrypted before being stored.  
The server supports multiple concurrent clients, logs all activities, and handles failures gracefully.

The project focuses on networking fundamentals, security principles, and system reliability.

---

## Key Features
- TCP-based client–server communication using Python sockets
- User authentication using username and password
- Binary-safe file transfer
- AES-based encryption for files at rest
- Persistent encryption key management
- Multi-client support using threading
- Server-side logging with timestamps
- Graceful error handling
- Automated unit tests

---

## Project Structure
secure_file_transfer/
│
├── client.py
├── server.py
├── crypto_utils.py
├── users.txt
├── README.md
├── .gitignore
│
└── tests/
    ├── __init__.py
    └── test_basic.py

---

## Requirements
- Python 3.9 or later
- cryptography library

Install dependency:
pip install cryptography

---

## How the System Works
1. The server listens for incoming TCP connections.
2. The client authenticates with username and password.
3. The client uploads a file in binary format.
4. The server encrypts the file before saving it.
5. The server logs all actions and errors.
6. Multiple clients are supported concurrently.

---

## How to Run

### Start the Server
python server.py

### Run the Client
python client.py

---

## Testing
Run unit tests from the project root:
python -m unittest discover

---

## Security Notes
- Files are encrypted before storage.
- Plaintext files are never stored on the server.
- Authentication is required before file transfer.

---

## Author
Aakriti
