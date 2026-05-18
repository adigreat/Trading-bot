import argparse
from colorama import Fore, init
from bot.orders import (
    place_market_order,
    place_limit_order,
    place_stop_order
)
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.logging_config import logger
init(autoreset=True)
def print_success(message):
    print(Fore.GREEN + message)

def print_error(message):
    print(Fore.RED + message)

def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price", required=False)
    parser.add_argument("--stopprice", required=False)
    args = parser.parse_args()
    try:
        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price)
        stop_price = validate_price(args.stopprice)
        print("\n========== ORDER REQUEST ==========")
        print(f"Symbol      : {symbol}")
        print(f"Side        : {side}")
        print(f"Type        : {order_type}")
        print(f"Quantity    : {quantity}")
        if price:
            print(f"Price       : {price}")
        if stop_price:
            print(f"Stop Price  : {stop_price}")
        print("===================================\n")
        if order_type == "MARKET":
            response = place_market_order(
                symbol,
                side,
                quantity
            )
        elif order_type == "LIMIT":
            if price is None:
                raise ValueError(
                    "LIMIT order requires --price"
                )
            response = place_limit_order(
                symbol,
                side,
                quantity,
                price
            )
        elif order_type == "STOP":
            if stop_price is None:
                raise ValueError(
                    "STOP order requires --stopprice"
                )
            response = place_stop_order(
                symbol,
                side,
                quantity,
                stop_price
            )
        print("\n========== ORDER RESPONSE ==========")
        print(f"Order ID       : {response.get('orderId')}")
        print(f"Status         : {response.get('status')}")
        print(f"Executed Qty   : {response.get('executedQty')}")
        print(f"Avg Price      : {response.get('avgPrice')}")

        print("====================================")
        print_success("\nOrder placed successfully!")
        logger.info("Order placed successfully")
    except Exception as e:

        logger.error(str(e))

        print_error(f"\nError: {e}")
if __name__ == "__main__":
    main()