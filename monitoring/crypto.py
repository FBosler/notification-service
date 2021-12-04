import json
from typing import Optional

import requests

URL = "https://api.avax.network/ext/bc/C/rpc"
PAYLOAD = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "eth_call",
    "params": [
        {
            "from": "0x0000000000000000000000000000000000000000",
            "data": "0xf7888aec000000000000000000000000130966628846bfd36ff31a822705796e8cb8c18d00000000000000000000000035fa7a723b3b39f15623ff1eb26d8701e7d6bb21",
            "to": "0xf4f46382c2be1603dc817551ff9a7b333ed1d18f",
        },
        "latest",
    ],
}
headers = {"content-type": "application/json"}

THRESHOLD = 500


def check(threshold: str = None) -> Optional[str]:
    used_threshold = threshold or THRESHOLD
    res = requests.post(URL, data=json.dumps(PAYLOAD), headers=headers)
    available_mim = int(res.json().get("result"), base=16) / 1e18

    if available_mim > used_threshold:
        msg = f"Currently available MIM: {available_mim}"
        print(msg)
        return msg
