"""
  Http Server
"""
from aiohttp import web
from src import handlers


def start_http_server():
    app = web.Application()
    app.add_routes(handlers.routes)
    web.run_app(app)
