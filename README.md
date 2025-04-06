# TCP Chat Server

![Network Chat](https://img.shields.io/badge/protocol-TCP-blue) ![Python](https://img.shields.io/badge/language-Python3-green) ![Multi-Client](https://img.shields.io/badge/support-Multi--Client-orange)

A simple yet powerful multi-client TCP chat server built with Python. Allows real-time messaging between multiple users via the command line. Ideal for learning networking basics or lightweight group communication.

---

## Features

- **Multi-Client Support**: Handle multiple users simultaneously using threading.
- **Real-Time Messaging**: Instant message broadcasting to all connected clients.
- **Clean Exit**: Type `exit` to disconnect gracefully.
- **Error Handling**: Robust connection/disconnection management.
- **Cross-Platform**: Works on Linux, macOS, and Windows.

---

## Requirements

- Python 3.6+ ([Download Python](https://www.python.org/downloads/))
- Basic terminal/command-line knowledge

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/kk3rn3l/tcp-chat-server.git
   cd tcp-chat-server
   ```

2. **Verify Python**:
   ```bash
   python3 --version  # Should output 3.6+
   ```

---

## Usage

### 1. Start the Server
Run the chat server (default: listens on all interfaces, port 5555):
```bash
python3 chat_server.py
```

### 2. Connect Clients
Open new terminals and connect clients:
```bash
python3 client.py
```

### 3. Start Chatting
- Type messages in any client terminal.
- Messages are broadcast to **all connected clients**.
- Type `exit` to disconnect a client.

![Demo](demo.gif) *(Optional: Add a GIF showing usage)*

---

## Configuration

Edit the following variables in `chat_server.py` and `client.py`:
- **Change Host**:
  ```python
  HOST = '0.0.0.0'  # Server: Bind to all interfaces
  HOST = 'localhost' # Client: Connect to local machine
  ```
- **Change Port**:
  ```python
  PORT = 5555  # Use any unused port (1024-65535)
  ```

---

## Troubleshooting

- **Port Conflicts**:
  ```bash
  netstat -tuln | grep 5555  # Check if port 5555 is free
  ```
- **Firewall Issues**:
  ```bash
  sudo ufw allow 5555/tcp  # Allow traffic on Ubuntu
  ```
- **Connection Refused**:
  - Ensure the server is running before clients connect.
  - Verify `HOST`/`PORT` match in both scripts.

---

## Security Note

⚠️ **This is a demo tool!** Do NOT expose it to the public internet.  
For production use:
- Add SSL/TLS encryption.
- Implement user authentication.
- Sanitize inputs to prevent attacks.

---

## Contributing

1. Fork the repository.  
2. Create a feature branch:  
   ```bash
   git checkout -b feature/new-feature
   ```
3. Commit changes:  
   ```bash
   git commit -m "Add new feature"
   ```
4. Push and submit a pull request.

---

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Acknowledgments

- Built with Python's `socket` and `threading` modules.
- Inspired by network programming fundamentals.

---
