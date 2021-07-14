import requests
from datetime import date

today = date.today()
print("Today:", today)

url = "http://172.17.0.2"
try:
    r = requests.head(url)
    print(r.status_code)
    print(r.headers)
    print(r.headers['Date'])

except requests.ConnectionError:
    print("failed to connect")
