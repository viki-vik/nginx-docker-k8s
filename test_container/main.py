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
    py_html_test.test_response("http://172.17.0.2")