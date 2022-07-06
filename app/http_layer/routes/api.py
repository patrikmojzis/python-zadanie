from ..controllers import price_controller, price_history_controller

def setup_routes(app):
    app.router.add_get('/price/history', price_history_controller.index)
    app.router.add_delete('/price/history', price_history_controller.destroy)
    app.router.add_get('/price/{currency}', price_controller.show)
