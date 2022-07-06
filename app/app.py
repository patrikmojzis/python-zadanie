from aiohttp import web
from http_layer.signals.headers_signal import setup_headers
from http_layer.signals.cors_signal import setup_cors
from database.database import setup_database
from http_layer.routes.api import setup_routes

async def init_app(argv=None):
    app = web.Application()

    setup_database(app)
    setup_routes(app)
    setup_cors(app)
    setup_headers(app)

    return app

def run():
	app = init_app()
	web.run_app(app, host='localhost', port=8000)

if __name__ == '__main__':
    run()