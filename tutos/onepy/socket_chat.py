
import random
from epyk.core.data import chartJs

# Socket server url
SERVER_SOCKET_HOST = "127.0.0.1"
SERVER_SOCKET_PORT = 5000


def get_page(page):
  print("Run the page")
  # Create the server configuration on the JavaScript Side
  server = page.data.js.server(SERVER_SOCKET_HOST, SERVER_SOCKET_PORT).addNamespace('news', alias="name")
  socket = page.js.socketio()
  socket.connect(from_config=server.getNamespace('name'))

  title = page.ui.title("Chat / News Listener")
  container = page.ui.network.news()
  input = page.ui.input()
  input.style.css.text_align = "left"
  input.style.css.padding_left = 5
  button = page.ui.button("Send").click([
    socket.emit("new news", input.dom.content),
    input.dom.empty()])
  input.enter([button.dom.events.trigger("click")])
  pie = page.ui.charts.chartJs.bar([], y_columns=[1], x_axis="x")
  row = page.ui.row([container, pie], position="top")
  row.options.responsive = False
  row.options.autoSize = False

  box = page.ui.div()
  box.extend([title, input, button, row])
  box.style.doc()

  container.subscribe(socket, 'news received', data=socket.message['content'])
  pie.subscribe(socket, 'news received', data=socket.message['pie'])


def get_series(count, size, negatives=0.1, missing=0.2):
  data = []
  neg = size * [False]
  miss = size * [False]
  for s in range(size):
    data.append({"x": s, 'r': random.randint(0, 10), 'g': random.randint(0, 5)})
    for c in range(count):
      if miss[s]:
        continue

      data[-1][c] = random.randint(0, 10000) / 100 * (-1 if neg[s] else 1)
  return data


if __name__ == "__main__":
  print("OK")
  import eventlet
  import socketio

  sio = socketio.Server(cors_allowed_origins='*')
  app = socketio.WSGIApp(sio)

  @sio.on('new news', namespace='/news')
  def new_news(sid, message):
    values = chartJs.y(get_series(5, 100), [1, 4, 5], 'g')
    sio.emit(
      'news received', {"content": message, 'pie': values}, broadcast=True, namespace='/news')

  @sio.event(namespace='/news')
  def disconnect(sid):
    print('disconnect ', sid)

  eventlet.wsgi.server(eventlet.listen((SERVER_SOCKET_HOST, SERVER_SOCKET_PORT)), app)
