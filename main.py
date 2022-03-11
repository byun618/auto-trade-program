from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import socketio

sio = socketio.AsyncServer(cors_allowed_origins="*", async_mode='asgi')
app = FastAPI()
socketio_app = socketio.ASGIApp(sio, app)

# origins = ["*"]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


@sio.event
def connect(sid, environ):
    print('connect ', sid)


@sio.on('message')
async def chat_message(sid, data):
    print("message ", data)
    await sio.emit('response', 'hi ' + data)


@app.get("/v2")
def read_main():
    return {"message": "Hello World"}
