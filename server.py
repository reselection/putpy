#!/bin/python3

import socket
import subprocess

HOST = "127.0.0.1"
PORT = 42061

def server():
    """Runs the server and recieves a message for execution"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                x = data.decode()
                try:
                    y = subprocess.Popen(x)
                except:
                    try:
                        conn.send(b"Invalid command")
                    except:
                        print("Cant send data") 
    server()
server()
