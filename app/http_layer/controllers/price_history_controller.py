import json
from aiohttp import web

from models.price import Price

async def index(request):
    page = max(request.rel_url.query.get('page', 0), 0)
    result_per_page = 10

    prices = request.app['db'].query(Price).limit(result_per_page).offset(page * result_per_page).all()

    payload = []
    for price in prices:
        payload.append({'pair': price.pair, 'last_bid_price': price.last_bid_price, 'date': price.created_at.strftime("%Y-%m-%d %H:%M:%S")})

    return web.Response(body=json.dumps(payload), status=200)

async def destroy(request):
    request.app['db'].query(Price).delete()
    request.app['db'].commit()
    return web.Response(status=204)