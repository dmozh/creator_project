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
from aiohttp import web

from .routes import setup_routes

async def create_app():
    app = web.Application()
    setup_routes(app)
    return app
"""

routes = \
"""
from .views import response
import credentials as crs

def setup_routes(app):
    #app.router.add_route('GET/POST', f'%url%', response.%func%)
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
"""

