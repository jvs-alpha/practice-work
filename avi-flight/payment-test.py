import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'Origin': 'https://flight-book-app.netlify.app',
    'Referer': 'https://flight-book-app.netlify.app/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

json_data = {
    'price': 10755,
    'adult': 1,
    'children': 1,
    'way': False,
}

response = requests.post('https://flightpayement.herokuapp.com/payment', headers=headers, json=json_data)
print(response.status_code, response.text)
