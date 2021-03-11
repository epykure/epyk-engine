
from epyk.core.data import events
from epyk.core.Page import Report

# Socket server url
SERVER_SOCKET_HOST = "127.0.0.1"
SERVER_SOCKET_PORT = 5000

from flask import Flask
app = Flask(__name__)


def get_page_flask():
  page = Report()
  page.headers.dev()

  title = page.ui.title("Flask - First example")
  input = page.ui.input(placeholder="Enter a text message", html_code="msg")
  button = page.ui.buttons.colored("Click")
  input.enter([button.dom.events.trigger("click")])
  button.click([page.js.post("/test_event", components=[input]).onSuccess([
    page.js.alert(events.data["message"])
  ])])

  box = page.ui.div()
  box.extend([title, input, button])
  box.style.doc()
  return page


if __name__ == "__main__":
  from flask import Flask, jsonify, request

  @app.route('/')
  def ui():
    return get_page_flask().outs.html()

  @app.route('/test_event', methods=['POST'])
  def test_event():
    data = request.get_json()
    return jsonify({"message": data['msg']})

  Flask.run(app, host=SERVER_SOCKET_HOST, port=SERVER_SOCKET_PORT, debug=True)
