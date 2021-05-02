
import epyk as pk
from epyk.tests import mocks

# Socket server url
SERVER_SOCKET_HOST = "127.0.0.1"
SERVER_SOCKET_PORT = 5000

from flask import Flask
app = Flask(__name__)


def create_page():
  page = pk.Page()
  page.body.template.style.configs.doc(background="white")

  stepper = page.ui.steppers.arrow([
    {"value": 'test 1', "status": 'pending', 'label': 'test'},
    {"value": 'test 2'},
    {"value": 'test 3', "status": 'waiting'}],
    options={"media": False, "line": False})
  page.ui.div(stepper, align="center")
  stepper[1].click([
    page.js.alert("This ")
  ])
  tabs = page.ui.panels.tabs()
  tabs.add_panel("Status 1", "Description for status 1", selected=True)
  tabs.add_panel("Status 2", "Description for status 2")
  tabs.add_panel("Status 3", "Description for status 3")

  btn1 = page.ui.button("Previous", icon="fas fa-caret-left")
  btn1.style.css.padding_h = 5
  btn1.click([
    stepper.dom[pk.std.var("state").r].waiting(),
    stepper.dom[pk.std.var("state")].arrow(),
    stepper.dom[pk.std.var("state")].text(""),
    stepper.dom[pk.std.var("state")].css({"border-bottom": "1px solid white", "padding-bottom": "5px"}),
    pk.std.var("state", pk.std.maths.max(pk.std.parseInt(pk.std.var("state")) - 1, 0), global_scope=True),
    stepper.dom[pk.std.var("state")].css({"border-bottom": "1px solid green", "padding-bottom": "5px"}),
    stepper.dom[pk.std.var("state")].triangle(),
    stepper.dom[pk.std.var("state")].pending(),
    stepper.dom[pk.std.var("state")].text("Pending", color="black"),
    tabs.dom[pk.std.var("state")].select(),
  ])

  btn2 = page.ui.button("Next", icon="fas fa-caret-right")
  btn2.style.css.padding_h = 5
  btn2.click([
    stepper.dom[pk.std.var("state")].success(),
    stepper.dom[pk.std.var("state")].arrow(),
    stepper.dom[pk.std.var("state")].css({"border-bottom": "1px solid white", "padding-bottom": "5px"}),
    pk.std.var("state", pk.std.maths.min(pk.std.parseInt(pk.std.var("state")) + 1, 2), global_scope=True),
    stepper.dom[pk.std.var("state")].css({"border-bottom": "1px solid green", "padding-bottom": "5px"}),
    stepper.dom[pk.std.var("state")].triangle(),
    stepper.dom[pk.std.var("state")].text("Pending", color="black"),
    tabs.dom[pk.std.var("state")].select(),
    page.js.console.log(tabs.dom[pk.std.var("state")].innerText())
  ])

  table = page.ui.table(mocks.popularity_2020)
  table.options.paginationSize = 10
  table.click([
    page.js.console.log(pk.events.data)
  ])
  page.body.onReady([
    pk.std.var("state", 0, global_scope=True)
  ])
  return page


if __name__ == "__main__":
  from flask import Flask, jsonify, request


  @app.route('/')
  def ui():
    return create_page().outs.html()

  Flask.run(app, host=SERVER_SOCKET_HOST, port=SERVER_SOCKET_PORT, debug=True)
