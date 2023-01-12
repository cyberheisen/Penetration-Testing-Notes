import socketio


debug = False
proxies = {'http':'http://127.0.0.1:8080','https':'https://127.0.0.1:8080'}
url = ''

# websocket event handlers

def login_success():
  print('Login successful')

@ws.on('connect')
def connect():
  print('Connection to %s is established' % url)

@ws.on('disconnect')
def disconnect():
  print('Websocket to %s closed' % url)

@ws.event
def message(data):
  print('message received: %s' % data['message'])

# connect via websocket
print("Connecting to %s via websocket" % url)

# check whether debug is enabled
# this will send websocket data through a proxy
if debug is True:
  session = requests.session()
  session.proxies = proxies
  ws = socketio.Client(http_session=session)
  else:
    ws = socketio.Client()

ws.connect(url)

# send a message
ws.emit("login",{"email":"test@example.com","password":"12345"})
# capture specific return event.. e.g.. "login_success"
# wait a bit for the response
time.sleep(2)
ws.on('login_success',login_success)

# close websocket
ws.disconnect
