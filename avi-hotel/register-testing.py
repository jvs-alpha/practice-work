import requests

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Access-Control-Request-Headers': 'content-type',
    'Access-Control-Request-Method': 'POST',
    'Connection': 'keep-alive',
    'Origin': 'https://smooth-hotel.netlify.app',
    'Referer': 'https://smooth-hotel.netlify.app/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
}

response = requests.options('https://mren-hotel.herokuapp.com/api/users/register', headers=headers)
