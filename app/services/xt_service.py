import ccxt.async_support as ccxt

async def get_last_bit_price(pair):
    exchange = ccxt.kucoin()
    ticker = await exchange.fetchOrderBook(pair)
    lastBid = ticker["bids"][0][0]
    await exchange.close()
    return lastBid