import asyncio, os, websockets
from threading import Thread
from django.apps import AppConfig

async def echo(websocket, path):
    async for message in websocket:
        print(f"Recebido: {message}")
        await websocket.send(f"Echo: {message} - Kekw")

def start_server():
    # Cria um novo loop de eventos para esta thread
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    start_server = websockets.serve(echo, "0.0.0.0", 6789)
    loop.run_until_complete(start_server)
    loop.run_forever()

class CertificateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'certificate'

    def ready(self):
        if os.environ.get('RUN_MAIN') == 'true':
            server_thread = Thread(target=start_server)
            server_thread.start()
            print("Servidor WebSocket iniciado em ws://localhost:6789")
