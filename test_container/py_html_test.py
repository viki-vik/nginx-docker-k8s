import requests
import datetime
from datetime import date
from streamlit import caching
# from dateutil import parser


def get_http_response(url):
    response_code = -1000
    try:
        r = requests.head(url)
        caching.clear_cache()
        r.cookies.clear()
        response_code = r.status_code
        # print("Response_code " + str(response_code))
    except requests.ConnectionError:
        print("Failed to connect")
    return response_code


def get_response_data(url, response_code):
    response_data = ''
    if response_code == 200:
        print("The web page is served correctly")
        try:
            r = requests.head(url)
            response_data = r.headers['Date']
            print("JS function returned date: " + response_data)
        except requests.ConnectionError:
            print("ConnectionError")
    return response_data

def extract_date(ret_date):
    # ret_date = '2021-07-22T12:06:16.903Z'
    js_date = ''
    try:
        js_date = datetime.datetime.strptime(str(ret_date)[:10], "%Y-%m-%d")
    except ValueError:
        print("Error: what is getting returned is not a date")
    return js_date

def check_date(js_date):
    py_date = date.today().strftime("%Y-%m-%d")
    print("Today:", py_date)
    if py_date == js_date:
        print("The returned date is correct")
    else:
        print("The returned date is incorrect")
