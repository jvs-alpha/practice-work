import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlQ0RFZETHZWOGpneU1NOWtsTXM0QSJ9.eyJpc3MiOiJodHRwczovL2Rldi1ydWgzbHAyMi51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTA1NTI1Nzk1MTk4MzM2MTg3NTIiLCJhdWQiOlsiaHR0cHM6Ly9zaG9ydGxpbmstZXhhbXBsZS5jb20iLCJodHRwczovL2Rldi1ydWgzbHAyMi51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjU3NTUzNDgzLCJleHAiOjE2NTc1NTcwODMsImF6cCI6IkhDV3laTTlnV2pOaU8wcXlkdVRBYlJkbVpKaks5MlJ2Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbXX0.MaKBHIL3Opbl0sYFE3oDFUVjOMkk2zt-OZ8nMT4-TS7o2Fbdc0eOIg5X6c2qdTldB6W0QF1NfSY8Gj5qFxpPgYmoDQYVxkBPxDJq6vu0yA3Xw76A5C9RQE7kfxodpsSHNCzUEiVkkcWJW1VNus-Wi-NGua-8ilRaQXshoxJeKyIBeH5mYCDGLpnbEkj-St7hfCsRhR0hGGQRG-03qmsZvqghPCIwZ0i-jyBxCNNOlg33jtbvhs3AqRDpHrt2KS46A1940pQWw0nYKT2o5vuHy4JP4KRX2Ouf6HgO987dLubupQ_xIM4ydbmJXWbv0L3WMfG8M1Tg1miO8RmrHGFbVw',
    'Connection': 'keep-alive',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'Origin': 'https://ygishortlink.netlify.app',
    'Referer': 'https://ygishortlink.netlify.app/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

json_data = {
    'name': 'jvs-hack1',
    'url': [
        {
            'link': 'https://ygi.li/',
        },
    ],
    'priority': '1',
    'multiple': 'false',
    'date': 1657553632722,
    'links': [
        {
            'link': 'https://ygi.li/',
        },
    ],
}

response = requests.post('https://ygi-shortlink.herokuapp.com/api/v1/shortlink/create', headers=headers, json=json_data)
print(response.text)