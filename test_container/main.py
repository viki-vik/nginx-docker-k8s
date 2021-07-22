########################################################
# created by:   Vika Baktov
# purpose:      container tests:
#               the web page is served correctly
#               what is getting returned is a date
#               the returned date is correct
# date:         14/07/21
# version:      1.3
########################################################

import py_html_test as pht
import subprocess as sp


if __name__ == '__main__':
    while True:
        try:
            url = sp.getoutput('minikube service --url kube-js-svc')
            print(f'Container running on {url}')
            response_code = pht.get_http_response(url)
            # pht.test_return_value(url, response_code)
            response_data = pht.get_response_data(url, response_code)
            js_date = pht.extract_date(response_data)
            pht.check_date(js_date)
        except ValueError:
            print('Error: check minikube is up and service is running')
        break

