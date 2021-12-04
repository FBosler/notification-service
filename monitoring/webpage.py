from typing import Optional

from bs4 import BeautifulSoup
import requests

URL = "https://www.everdrop.de/products/handburste-aus-fsc-zertifiziertem-buchenholz-und-pflanzlichen-borsten"
# URL = "https://www.everdrop.de/products/everdrop-glastiegel" (this one is available at time of writing)


def find_add_to_cart_button(url: str = None) -> Optional[str]:
    target_url = url or URL
    res = requests.get(target_url)
    soup = BeautifulSoup(res.content, "html.parser")

    # you will need to adjust this to your definition use right-click -> inspect element
    # to get information to identify your destination
    # More documentation here https://www.crummy.com/software/BeautifulSoup/bs3/documentation.html#arg-attrs
    add_to_cart_button = soup.findAll(attrs={"data-node-type": "commerce-add-to-cart-button"})

    if add_to_cart_button:
        msg = "Found an add-to-cart-button"
        print(msg)
        return msg
