import time
import requests
from login import get_auth_token

headers = {
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'Authorization': '',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://onlinebusiness.icbc.com/webdeas-ui/booking',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

json_data = {
    'aPosID': 153, # Langley
    'examType': '5-R-1',
    'examDate': '2022-07-20',
    'ignoreReserveTime': False,
    'prfDaysOfWeek': '[0,1,2,3,4,5,6]',
    'prfPartsOfDay': '[0,1]',
    'lastName': 'HAN',
    'licenseNumber': '2163482',
}

def is_wanted(date) -> bool:
    tokens = date.split('-')
    year = tokens[0]
    month = tokens[1]
    day = tokens[2]
    if year != "2022":
        return False

    # all 2022 dates
    if month == '07':
        return True
    elif month == "08" and day < "24":
        return True

    return False

def get_latest_time():
    response = requests.post('https://onlinebusiness.icbc.com/deas-api/v1/web/getAvailableAppointments', headers=headers, json=json_data)
    status_code = response.status_code
    if status_code == 403:
        print("403 found. Attempting to login again")
        token = get_auth_token()
        print("Token:",)
        headers['Authorization'] = token
        get_latest_time()
        return

    # The logic below would only work when status_code == 200
    print(status_code)
    body = response.json()

    best_time: str = ""
    for item in body:
        appt = item['appointmentDt']
        date = appt['date']
        start_time = item['startTm']
        date_time = f"{date} -> {start_time}"
        # print(date_time)
        if best_time == "":
            best_time = date_time

        if is_wanted(date):
            best_time = date_time

    print("> ", best_time)


if __name__ == '__main__':
    while True:
        get_latest_time()
        time.sleep(5)
