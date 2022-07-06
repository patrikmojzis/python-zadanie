import json
from aiohttp import web
from services.time_service import round_seconds
from models.price import Price
from services import xt_service
import datetime as dt

async def show(request):
    currency = request.match_info['currency']
    try:
        pair = f'{currency.upper()}-USDT'
        last_bid_price = await xt_service.get_last_bit_price(pair)

        price = Price(pair = pair, last_bid_price = last_bid_price, created_at = round_seconds(dt.datetime.now()))
        request.app['db'].add(price)
        request.app['db'].commit()
        
        return web.Response(body=json.dumps({'last_bid_price': last_bid_price}), status=200)
    except Exception as e:
        return web.HTTPBadRequest(text=json.dumps({'error': 'InvalidPair', 'message': str(e)}))