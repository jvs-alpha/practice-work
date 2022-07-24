# import requests
#
# r = requests.get("http://behavehierarchical.za.com/indiapost/tb.php?_t=16496603691649660736302")

import requests
import threading
import time
import sys
import logging


def send_request_fn():
    headers = {
        'authority': 'ag0uuz.cn',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://behavehierarchical.za.com/',
        'accept-language': 'en-GB,en;q=0.9',
    }

    params = {
        '_t': '1649691119912',
    }
    # response = requests.get('https://ag0uuz.cn/ObhsB2uH/indiapost/', headers=headers, params=params)
    response = requests.get('http://behavehierarchical.za.com/indiapost/t', headers=headers, params=params)
    print(response.text)

send_request_fn()

# counter = 0
# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)
# while True:
#     try:
#         counter += 1
#         send_request_fn()
#     except:
#         logging.info(counter)
#         sys.exit()

