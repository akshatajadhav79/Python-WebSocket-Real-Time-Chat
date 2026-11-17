from starlette.types import Receive
from email import message
from threading import active_count
from fastapi import FastAPI, WebSocket,WebSocketDisconnect

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections = {}

    async def connect(self,username:str,websocket:WebSocket):
        await websocket.accept()
        self.active_connections[username] = websocket
        print(f"{username} connected.")

    def disconnect(self,username:str):
        if  username in self.active_connections:
            del self.active_connections[username]
        print(f"{username} disconnected")

        # Send private message
    async def send_message(self, receiver: str, message: str):
        if receiver in self.active_connections:
            websocket = self.active_connections[receiver]
            await websocket.send_json({
                "from": "message",
                "message": message
            })
            return True
        return False


manager = ConnectionManager()


@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket:WebSocket,username:str):
    await manager.connect(username,websocket)
    try:
        while True:
            # msg from client
            data = await websocket.receive_json()
            print(data)

            receiver = data.get("to")
            message = data.get("message")

            if not receiver or not message:
                await websocket.send_json({
                    "from":"server",
                    "message":"Receiver and message are required"
                })
                continue

            # send msg to client
            success = await manager.send_message(
                receiver,message
            )
            if success:
                await websocket.send_json({"from":"server","message":f"Message delivered to {receiver}"})
            else:
                await websocket.send_json({"from":"server","message":f"{receiver} is offline"})
    except WebSocketDisconnect:
        manager.disconnect(username)
        print("client disconnect")

@app.get("/")
def health():
    return {"message":"WhatsApp-like Chat Server Running"}
