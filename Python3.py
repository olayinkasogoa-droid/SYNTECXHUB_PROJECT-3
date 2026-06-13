crypto.utiles.py

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

with open("key.txt", "rb") as f:
    KEY = f.read().strip()

def encrypt_message(message):
    iv = get_random_bytes(16)

    cipher = AES.new(
        KEY,
        AES.MODE_CFB,
        iv=iv
    )

    ciphertext = cipher.encrypt(
        message.encode()
    )

    encrypted_data = iv + ciphertext

    return base64.b64encode(
        encrypted_data
    )

def decrypt_message(encrypted_data):
    data = base64.b64decode(
        encrypted_data
    )

    iv = data[:16]

    ciphertext = data[16:]

    cipher = AES.new(
        KEY,
        AES.MODE_CFB,
        iv=iv
    )

    plaintext = cipher.decrypt(
        ciphertext
    )

    return plaintext.decode()

Server.py

import socket
import threading
import logging

from crypto_utils import (
    encrypt_message,
    decrypt_message
)

HOST = "0.0.0.0"
PORT = 5555

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

logging.basicConfig(
    filename="chat.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

print(f"[+] Server listening on {HOST}:{PORT}")

def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            pass

def remove_client(client):
    if client in clients:
        index = clients.index(client)

        nickname = nicknames[index]

        clients.remove(client)
        nicknames.remove(nickname)

        client.close()

        leave_message = f"{nickname} left the chat."

        print(leave_message)

        logging.info(leave_message)

        broadcast(
            encrypt_message(leave_message)
        )

def handle_client(client):
    while True:
        try:
            encrypted_message = client.recv(4096)

            if not encrypted_message:
                break

            plaintext = decrypt_message(
                encrypted_message
            )

            print(plaintext)

            logging.info(plaintext)

            broadcast(
                encrypt_message(plaintext)
            )

        except Exception:
            break

    remove_client(client)

def receive_connections():
    while True:

        client, address = server.accept()

        print(
            f"[+] Connected: {address}"
        )

        client.send(
            encrypt_message("NICK")
        )

        encrypted_nick = client.recv(4096)

        nickname = decrypt_message(
            encrypted_nick
        )

        nicknames.append(nickname)
        clients.append(client)

        join_msg = (
            f"{nickname} joined the chat."
        )

        print(join_msg)

        logging.info(join_msg)

        broadcast(
            encrypt_message(join_msg)
        )

        thread = threading.Thread(
            target=handle_client,
            args=(client,)
        )

        thread.start()

receive_connections()

Client.py

import socket
import threading

from crypto_utils import (
    encrypt_message,
    decrypt_message
)

HOST = input(
    "Server IP: "
)

PORT = 5555

nickname = input(
    "Nickname: "
)

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect((HOST, PORT))

def receive():
    while True:
        try:
            encrypted = client.recv(4096)

            message = decrypt_message(
                encrypted
            )

            if message == "NICK":

                client.send(
                    encrypt_message(
                        nickname
                    )
                )

            else:
                print(message)

        except:
            print(
                "Disconnected."
            )

            client.close()

            break

def write():
    while True:
        text = input()

        message = (
            f"{nickname}: {text}"
        )

        encrypted = encrypt_message(
            message
        )

        client.send(encrypted)

receive_thread = threading.Thread(
    target=receive
)

write_thread = threading.Thread(
    target=write
)

receive_thread.start()
write_thread.start()

