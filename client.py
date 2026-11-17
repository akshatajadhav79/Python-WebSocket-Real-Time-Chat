
import asyncio
import websockets
import json


async def receive_messages(websocket):

    try:
        while True:

            response = await websocket.recv()

            data = json.loads(response)

            print(f"\n[{data['from']}] {data['message']}")
            print("You: ", end="", flush=True)

    except websockets.exceptions.ConnectionClosed:
        print("\nDisconnected from server")


async def chat():

    username = input("Enter your username: ").strip()

    uri = f"ws://127.0.0.1:8000/ws/{username}"

    try:

        async with websockets.connect(uri) as websocket:

            print(f"\nWelcome {username}!")
            print("Connected to chat server.")
            print("Send message: /to username message")
            print("Exit: /quit\n")

            receiver_task = asyncio.create_task(
                receive_messages(websocket)
            )

            try:

                while True:

                    message = await asyncio.to_thread(
                        input, "You: "
                    )

                    if message.strip() == "/quit":
                        break

                    if not message.startswith("/to "):
                        print("Use: /to username message")
                        continue

                    parts = message.split(" ", 2)

                    if len(parts) < 3:
                        print("Enter receiver and message")
                        continue

                    receiver = parts[1]
                    text = parts[2]

                    await websocket.send(json.dumps({
                        "to": receiver,
                        "message": text
                    }))

            finally:

                receiver_task.cancel()

    except (OSError, websockets.exceptions.WebSocketException) as e:

        print("Connection error:", e)


if __name__ == "__main__":
    asyncio.run(chat())
