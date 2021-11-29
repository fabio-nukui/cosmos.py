from cosmos_sdk.client.lcd import LCDClient
from cosmos_sdk.client.lcd.params import PaginationOptions
from cosmos_sdk.core import Coin, Coins
from cosmos_sdk.core.bank import MsgSend
from cosmos_sdk.util.contract import get_code_id


def main():
    terra = LCDClient(
        url="https://bombay-lcd.terra.dev/",
        chain_id="bombay-12",
    )

    pagOpt = PaginationOptions(limit=2, count_total=True)
    result = terra.bank.balance(
        address="terra1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v", params=pagOpt
    )
    print(result)
    result = terra.bank.balance(address="terra1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v")
    print(result)
    result = terra.bank.total(pagOpt)
    print(result)
    result = terra.bank.total()
    print(result)


main()
