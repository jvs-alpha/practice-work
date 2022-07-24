import requests

headers = {
    'Host': 'mren-hotel.herokuapp.com',
    # 'Content-Length': '143',
    'Sec-Ch-Ua': '" Not A;Brand";v="99", "Chromium";v="96"',
    'Accept': 'application/json, text/plain, */*',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Sec-Ch-Ua-Platform': '"Linux"',
    'Origin': 'https://smooth-hotel.netlify.app',
    'Referer': 'https://smooth-hotel.netlify.app/',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://smooth-hotel.netlify.app/',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    #'Connection': 'close',
}

json_data = {
    'userid': '62716908e5c1c2bc4745bd1c',
    'description': 'hello',
    'name': 'user',
    'roomid': '6274d29ac86b6c1f6c702f4c',
    'date': '2022-05-24T11:43:27.898Z',
}

response = requests.post('https://mren-hotel.herokuapp.com/api/reviews/addreview', headers=headers, json=json_data, verify=False)
