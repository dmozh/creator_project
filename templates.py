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
from .api import http, websocket
import credentials as crs


def setup_routes(app):
    app.router.add_route('GET', f'/test_get', http.get_api.test_get.test_json)
    app.router.add_route('POST', f'/test_post', http.post_api.test_post.test_json)
"""

views_init = \
    """
from . import http, websocket
"""

http_init = """from . import get_api, post_api, http_response"""
websocket_init = """from . import ws_response"""

get_api_init = """from . import test_get"""
post_api_init = """from . import test_post"""

test_get = """
from app.sql.sql_handler import sql_exec as handle
from aiohttp import web
import json


async def test_json(request):
    headers = {'Access-Control-Allow-Origin': '*'}
    if request.method == 'GET':
        response_msg = {}

        response_msg['msg'] = 'test'
        response_msg['method'] = 'get'
        return web.json_response(response_msg, headers=headers)
"""
test_post = """
from app.sql.sql_handler import sql_exec as handle
from aiohttp import web
import json


async def test_json(request):
    headers = {'Access-Control-Allow-Origin': '*'}
    if request.method == 'POST':
        response_msg = {}

        response_msg['msg'] = 'test'
        response_msg['method'] = 'post'
        return web.json_response(response_msg, headers=headers)
"""

http_response = \
    """
from app.sql.sql_handler import sql_exec as handle
from aiohttp import web
import json


async def test(request):
    headers = {'Access-Control-Allow-Origin': '*', 'content-type': 'text/html'}
    response = f'<div>test</div>'
    return web.Response(body=response, headers=headers)
"""

ws_response = \
    """
from aiohttp import web, WSMsgType
import json, asyncio


async def broadcast(request, msg):
    # while True:
    for ws in request.app.wslist:
        await ws.send_str(msg)
    # await asyncio.sleep(10)

async def websocket_handler(request):

    ws = web.WebSocketResponse()
    await ws.prepare(request)
    print(request.url)
    request.app.wslist.append(ws)
    print(request.app.wslist)
    async for msg in ws:
        print(msg)
        if msg.type == WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                print(msg.data)
                #await broadcast(request, tmp_val)
                await ws.send_str(msg.data + '/answer')
        elif msg.type == WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())

    print('websocket connection closed')
    print(ws)
    return ws"""

sql_handler = \
    """
#imports
#
#


async def sql_exec(query, **kwargs):
    '''
    Function to handle sql queries
    :param query: string key query
    :param kwargs: dict any kwargs
    :return: bool, json
    '''
    pass
"""

logger_template = '''
import logging
import logging.config
import os


def init_logger():
    """
    Инициализция логера
    :return:
    """
    if os.path.exists("logs"):
        pass
    else:
        os.mkdir("logs")
    logging.config.fileConfig('logger.conf')
    print("Init loggers")
    return logging.getLogger("infoLogger"), logging.getLogger("errorLogger")


def generate_message(prefix_msg: str, msg: str, **kwargs):
    """
    Генерация сообщения лога для журнала
    :param prefix_msg: str
    :param msg: str
    :param kwargs: dict
    :return: str
    """
    msg = f"{prefix_msg}: {msg} \n"
    if kwargs:
        # print(kwargs)
        msg += f"Additional info:"
        for key, value in kwargs.items():
            msg += f"\n{key}: {value}"
    return msg


info_logger, traceback_logger = init_logger()
'''

logger_conf = '''
[loggers]
keys=root,infoLogger,errorLogger

[handlers]
keys=fileInfoHandler,fileErrorHandler,consoleHandler

[formatters]
keys=myFormatter

[logger_root]
level=CRITICAL
handlers=consoleHandler

[logger_infoLogger]
level=INFO
handlers=fileInfoHandler
qualname=infoLogger

[logger_errorLogger]
level=ERROR
handlers=fileErrorHandler
qualname=errorLogger

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=myFormatter
args=(sys.stdout,)

[handler_fileInfoHandler]
class=FileHandler
formatter=myFormatter
args=("logs/info.log",)

[handler_fileErrorHandler]
class=FileHandler
formatter=myFormatter
args=("logs/error.log",)

[formatter_myFormatter]
format=%(asctime)s - %(name)s - %(filename)s - %(levelname)s - %(message)s
datefmt=
'''

requirements = """
cryptography
aiohttp
aiohttp_session
gunicorn
#pyodbc
#psycopg2
"""
