import requests
from datetime import date


# def get_url():
#     return url

# def test_date():
#     return


def test_response(url):
    today = date.today()
    print("Today:", today)

    try:
        r = requests.head(url)
        print(r.status_code)
        #        print(r.headers)
        print(r.headers['Date'])

    except requests.ConnectionError:
        print("failed to connect")