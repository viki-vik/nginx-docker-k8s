########################################################
# created by:   Vika Baktov
# purpose:      container tests:
#               the web page is served correctly
#               what is getting returned is a date
#               the returned date is correct
# date:         14/07/21
# version:      1.0
########################################################

import py_html_test

if __name__ == '__main__':
    while True:
        try:
            container_ip = py_html_test.get_container_ip()
        except ValueError:
            print('Error!!! Please insert Container IP in a valid format!!! Try again')
        break
    while True:
        try:
            port = str(py_html_test.get_port())
        except ValueError:
            print('Error!!! Please insert port number!!! Try again')
        break
    url = "http://" + container_ip  # + ":" + port
    print(url)
    py_html_test.test_response("url")