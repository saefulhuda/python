# queue = ['Data 1', 'Data 2', 'Data 3', 'Data 4']
# queue.copy()
# queue.append('Data tambahan')
# queue.remove('Data 4')
# print(queue)
# print(len(queue))


#HTTP Client module
import urllib.request
import urllib.error
import urllib.parse
import base64
import socket
import random
import signal
import time, datetime
import threading

def HTTPRequest(url, params, method = 'GET', auth = [], timeout = 10, headers = [], disableSSLCheck = False):
    setTimeout = timeout
    result  = {'http_code':'', 'message':'', 'results':[]}
    data    = []

    if method == 'POST':
        data = urllib.parse.urlencode(params)
        data = data.encode('ascii')
        request = urllib.request.Request(url, data)
    elif method == 'GET':
        data = urllib.parse.urlencode(params)
        request = urllib.request.Request(url + '?' + data)
    

    if len(auth) > 1 :
        base64string = base64.b64encode(bytes('%s:%s' % (auth[0], auth[1]),'ascii'))
        request.add_header("Authorization", "Basic %s" % base64string.decode('utf-8'))

    try:
        response = urllib.request.urlopen(request, timeout = setTimeout)
    except urllib.error.HTTPError as e:
        result['http_code'] = e.code
        if e.code == 404:
            result['message'] = 'URL Not Found'
    except urllib.error.URLError as e:
        if result['http_code'] == 408:
            result['message'] = e.reason
        else:
            result['message'] = 'URLError'
    except socket.timeout:
        result['http_code'] = 408
        result['message']   = 'Request Timeout'
    else:
        result['http_code'] = response.getcode()
        result['results'] = response.read()
    print(result)

def stopping(signum, stack_frame):
    print('I have encountered the signal KILL.')
    print('CTRL+C was pressed.  Do anything here before the process exists')
    exit()

signal.signal(signal.SIGINT, stopping)

while True:
    retry = random.choice(['1', '2', '0'])
    print(datetime.datetime.now())
    t = threading.Thread(target=HTTPRequest, args=('http://127.0.0.1/transport/send_mt_hutc.php', {'data':'This is test', 'retry':retry}, 'POST', [], 60))
    t.start()
    time.sleep(1)