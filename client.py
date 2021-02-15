#!/bin/python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 42061        # The port used by the server

def send_command():
    """
    Creates a connection and sends user input.
    """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    while True:
        cmd = input("Enter command: ")
        client.send(cmd.encode())

send_command()
