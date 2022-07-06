async def on_prepare(request, response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    # response.headers['Access-Control-Expose-Headers'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'false'

def setup_cors(app):
    app.on_response_prepare.append(on_prepare)