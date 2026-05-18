from binance.exceptions import BinanceAPIException
from bot.client import get_client
from bot.logging_config import logger
client = get_client()
def place_market_order(symbol, side, quantity):
    try:
        logger.info(
            f"MARKET ORDER -> {symbol} {side} {quantity}"
        )
        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
        logger.info(f"Response: {response}")
        return response
    except BinanceAPIException as e:
        logger.error(f"Binance Error: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise
def place_limit_order(symbol, side, quantity, price):
    try:
        logger.info(
            f"LIMIT ORDER -> {symbol} {side} {quantity} @ {price}"
        )
        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )
        logger.info(f"Response: {response}")
        return response
    except BinanceAPIException as e:
        logger.error(f"Binance Error: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise
def place_stop_order(symbol, side, quantity, stop_price):
    try:
        logger.info(
            f"STOP ORDER -> {symbol} {side} {quantity} STOP @ {stop_price}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="STOP_MARKET",
            stopPrice=stop_price,
            quantity=quantity
        )
        logger.info(f"Response: {response}")
        return response
    
    except BinanceAPIException as e:
        logger.error(f"Binance Error: {e}")
        raise
    
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise