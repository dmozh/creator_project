entry = \
"""  
from aiohttp import web
import argparse
from app import create_app
parser = argparse.ArgumentParser(description="aiohttp server example")
parser.add_argument('--path')
parser.add_argument('--port')
app = create_app()
if __name__ == '__main__':
    args = parser.parse_args()
    print(args.path, args.port)
    web.run_app(app, path=args.path, port=args.port)
"""

credentials = \
"""
#this file uses for creds to project
#its need add to git ignore
"""

utils = \
"""
#this file have util function
"""

app_init = \
"""
from .app import create_app
"""

app = \
"""
import base64
from cryptography import fernet
from aiohttp import web
from aiohttp_session import setup, get_session, session_middleware
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from .routes import setup_routes

#simple create app
async def create_app():
    app = web.Application()
    setup_routes(app)
    return app
    
#create app for using ws
#async def create_app():
#    app = web.Application()
#    fernet_key = fernet.Fernet.generate_key()
#    secret_key = base64.urlsafe_b64decode(fernet_key)
#    setup(app, EncryptedCookieStorage(secret_key))
#    setup_routes(app)
#    app.wslist = []
#    return app    
"""

routes = \
"""
from .views import response
import credentials as crs

def setup_routes(app):
    #app.router.add_route('GET/POST', f'%url%', response.%func%)
    #app.router.add_route('GET/POST', f'%url%', response.websocket_handler)
    pass
"""

views_init = \
"""
from . import response
"""

response = \
"""
from aiohttp import web
import json

# this file using for response from server

async def test(request):
    headers = {'Access-Control-Allow-Origin': '*', 'content-type': 'text/html'}
    response = f'<div>test</div>'
    return web.Response(body=response, headers=headers)
    
async def test_json(request):
    headers = {'Access-Control-Allow-Origin': '*'}
    if request.method == 'POST':
        response_msg = {}
        
        response_msg['msg'] = 'test'
        return web.json_response(response_msg, headers=headers)
    else:
        return web.Response(text='get', headers=headers)
        
async def broadcast(request, msg):
    # while True:
    for ws in request.app.wslist:
        await ws.send_str(msg)
    # await asyncio.sleep(10)
        
async def websocket_handler(request):

    ws = web.WebSocketResponse()
    await ws.prepare(request)
    print(request.url)
    async for msg in ws:
        print(msg)
        if msg.type == WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                print(msg.data)
                await ws.send_str(msg.data + '/answer')
        elif msg.type == WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())

    print('websocket connection closed')
    print(ws)
    return ws
"""

