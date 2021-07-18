import requests
from datetime import date


def get_container_ip():
    container_ip = input('Please insert Container IP: ')
    return container_ip

def get_port():
    port = input('Please insert port: ')
    return port

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