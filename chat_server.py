#!/usr/bin/env python3
import socket
import threading

# Configuration
HOST = '0.0.0.0'
PORT = 5555
MAX_CLIENTS = 10
clients = []

def broadcast(message, sender_socket=None):
    """Send message to all connected clients except sender"""
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                clients.remove(client)

def handle_client(client_socket):
    """Handle individual client connections"""
    try:
        while True:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"Received: {message}")
            broadcast(message, client_socket)
    except:
        pass
    finally:
        clients.remove(client_socket)
        client_socket.close()

def start_server():
    """Main server function"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(MAX_CLIENTS)
    print(f"[*] Chat Server listening on {HOST}:{PORT}")

    try:
        while True:
            client_socket, addr = server.accept()
            print(f"[+] New connection from {addr}")
            clients.append(client_socket)
            client_thread = threading.Thread(
                target=handle_client, 
                args=(client_socket,)
            )
            client_thread.start()
    except KeyboardInterrupt:
        print("\n[*] Shutting down server...")
    finally:
        server.close()

if __name__ == "__main__":
    start_server()
