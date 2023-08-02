import time
import requests

base_url = "http://api.open-notify.org/iss-now.json"

while True:
    iss_position = requests.get(base_url).json()['iss_position']
    result = f"{iss_position['longitude']};{iss_position['latitude']}\n"
    with open('iss_position_data.csv', 'a') as file:
        file.write(result)
    print(result, end="")
    time.sleep(5)
