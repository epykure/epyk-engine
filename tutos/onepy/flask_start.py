
import epyk as pk

# Socket server url
SERVER_SOCKET_HOST = "127.0.0.1"
SERVER_SOCKET_PORT = 5000

from flask import Flask
app = Flask(__name__)


def create_page():
  page = pk.Page()
  page.headers.dev()

  title = page.ui.title("Flask - First example")
  input = page.ui.inputs.left(placeholder="Enter your name", html_code="msg")
  button = page.ui.buttons.colored("Click")
  text = page.ui.text()
  simple_modal = page.ui.modals.popup([text])
  input.enter([button.dom.events.trigger("click")])
  button.click([page.js.post("/test_event", components=[input]).onSuccess([
    text.build(pk.events.data["message"]),
    simple_modal.dom.show()
  ])])

  box = page.ui.div()
  box.extend([title, input, button])
  box.style.configs.doc()
  return page


if __name__ == "__main__":
  from flask import Flask, jsonify, request

  @app.route('/')
  def ui():
    return create_page().outs.html()

  @app.route('/test_event', methods=['POST'])
  def test_event():
    data = request.get_json()
    return jsonify({"message": "Hello %s" % data['msg']})

  Flask.run(app, host=SERVER_SOCKET_HOST, port=SERVER_SOCKET_PORT, debug=True)
