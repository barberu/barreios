"""
  Http Server
"""
from aiohttp import web
from src import handlers

app = web.Application()
app.add_routes(handlers.routes)
web.run_app(app)
