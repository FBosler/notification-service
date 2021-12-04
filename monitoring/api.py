from typing import Optional
from numbers import Number
from xml.dom.minidom import parseString
import requests

SETTINGS = {
    "currency": "THB",
    "threshold": 35,
    "message": "The current exchange rate for EUR/{currency} is {value}",
}

URL = "http://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"


def check_exchange_rate(currency: str = None, threshold: Number = None) -> Optional[str]:
    res = requests.get(URL)

    # we have to parse XML (unfortunately I did not find a .json API)
    parsed = parseString(str(res.content.decode("utf-8")).replace("\n", "").replace("\t", ""))
    currency_rates = parsed.childNodes[0].childNodes[2].childNodes[0].childNodes

    target_currency = currency or SETTINGS.get("currency")
    target_threshold = threshold or SETTINGS.get("threshold")

    for currency_rate in currency_rates:
        currency = currency_rate.getAttribute("currency")
        rate = float(currency_rate.getAttribute("rate"))
        if currency == target_currency and rate > target_threshold:
            msg = SETTINGS.get("message").format(currency=currency, value=rate)
            print(msg)
            return msg


if __name__ == "__main__":
    check_exchange_rate()
