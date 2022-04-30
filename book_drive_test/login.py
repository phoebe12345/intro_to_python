import requests

headers = {
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'pragma': 'no-cache',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'Accept': 'application/json, text/plain, */*',
    'Cache-control': 'no-cache, no-store',
    'Referer': 'https://onlinebusiness.icbc.com/webdeas-ui/login;type=driver',
    'sec-ch-ua-platform': '"macOS"',
    'Expires': '0',
}

json_data = {
    'drvrLastName': 'han',
    'licenceNumber': '2163482',
    'keyword': 'ying',
}

def get_auth_token():
    response = requests.put('https://onlinebusiness.icbc.com/deas-api/v1/webLogin/webLogin', headers=headers, json=json_data)
    token = response.headers["Authorization"]
    return token

# get_auth_token()
