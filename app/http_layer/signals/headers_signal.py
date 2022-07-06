async def on_prepare(request, response):
    response.headers['Content-Type'] = 'application/json'

def setup_headers(app):
    app.on_response_prepare.append(on_prepare)