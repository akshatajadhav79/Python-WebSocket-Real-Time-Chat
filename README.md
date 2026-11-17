# Real-Time Chat Application Using Python WebSockets

## Project Overview

This project is a simple real-time, one-to-one chat application developed using Python, FastAPI, and WebSockets.

It allows two different users to connect to a common server through separate terminal sessions and exchange messages instantly without refreshing or repeatedly requesting the server.

The application uses persistent WebSocket connections to enable bidirectional communication between clients and the server.

## Technologies Used

- **Python 3.11+** – Programming language
- **FastAPI** – Backend framework
- **WebSockets** – Real-time bidirectional communication
- **Uvicorn** – ASGI server
- **Asyncio** – Asynchronous programming
- **JSON** – Message data exchange

## Project Structure

```text
whatsapp_chat/
│
├── main.py              # FastAPI WebSocket server
├── client.py            # Python WebSocket client
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Features

- Real-time communication between two users.
- Multiple users can connect simultaneously.
- Unique username-based connections.
- Private one-to-one messaging.
- Instant message delivery to online users.
- Online connection management.
- Handles user disconnections.
- Notifies the sender when the recipient is offline.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd whatsapp_chat
```

### 2. Create a Virtual Environment

```bash
python -m venv Nenv
```

Activate the environment on Windows:

```powershell
Nenv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install fastapi uvicorn websockets
```

Alternatively, install using:

```bash
pip install -r requirements.txt
```

### 4. Start the FastAPI Server

```bash
uvicorn main:app --reload
```

Server URL:

```text
http://127.0.0.1:8000
```

WebSocket endpoint:

```text
ws://127.0.0.1:8000/ws/{username}
```

### 5. Connect User 1

Open a new terminal:

```bash
python client.py
```

Enter username:

```text
akshata
```

### 6. Connect User 2

Open another terminal:

```bash
python client.py
```

Enter username:

```text
sahil
```

## How to Send Messages

Use the following command format:

```text
/to receiver_username your_message
```

Example:

**User 1 (akshata):**

```text
You: /to sahil Hello Sahil!
```

**User 2 (sahil):**

```text
[message] Hello Sahil!
```

**User 2 (sahil) replies:**

```text
You: /to akshata Hi Akshata!
```

**User 1 (akshata) receives:**

```text
[message] Hi Akshata!
```

## How It Works

1. The FastAPI server starts and listens for WebSocket connections.
2. Each user connects using a unique username.
3. The ConnectionManager maintains active WebSocket connections in a Python dictionary.
4. When a user sends a message, the server identifies the intended recipient.
5. The server forwards the message directly to the recipient's active WebSocket connection.
6. If the recipient is offline, the sender receives an offline notification.
7. When a user disconnects, their connection is removed from the active connection dictionary.

## Key Concepts Learned

- WebSocket protocol and persistent connections.
- HTTP vs WebSocket communication.
- FastAPI WebSocket endpoints.
- Asynchronous programming using `async` and `await`.
- Python asyncio tasks.
- WebSocket connection management.
- JSON serialization and deserialization.
- Real-time private messaging.
- Exception handling using WebSocketDisconnect.

## Future Enhancements

- User registration and login authentication using JWT.
- PostgreSQL database integration.
- Store and retrieve chat history.
- Message delivery and read receipts.
- Online and offline user status.
- Typing indicators.
- Group messaging.
- React-based chat interface.
- Redis integration for distributed WebSocket connections.

## Limitations

- Usernames are not authenticated.
- Messages are not stored permanently.
- Offline message delivery is not supported.
- Active connections are maintained in application memory.
- The current implementation is intended for learning and demonstration purposes, not production deployment.

## Conclusion

This project demonstrates how to build a basic real-time messaging system using Python WebSockets and FastAPI. It provides practical experience with asynchronous programming, persistent client-server connections, and private message delivery.