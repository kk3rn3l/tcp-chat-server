#!/usr/bin/env python3
import socket
import threading

HOST = 'localhost'
PORT = 5555

def receive_messages(client_socket):
    """Handle incoming messages from server"""
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
        print(f"Connected to {HOST}:{PORT} (type 'exit' to quit)")
        
        # Start receive thread
        receive_thread = threading.Thread(
            target=receive_messages,
            args=(client,)
        )
        receive_thread.start()
        
        # Handle user input
        while True:
            message = input()
            if message.lower() == 'exit':
                break
            client.send(message.encode())
            
    finally:
        client.close()

if __name__ == "__main__":
    start_client()
