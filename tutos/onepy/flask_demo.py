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

  table = page.ui.table(mocks.popularity_2020)
  table.options.paginationSize = 10

  toggle = page.ui.toggle({"on": "Trend", "off": "Share"}, html_code="toggle")
  bar = page.ui.charts.bar(mocks.popularity_2020, y_columns=["Share"], x_axis="Language")

  toggle.click([
    page.js.post("/data", components=[toggle.input]).onSuccess([
      bar.build(pk.events.data["chart_data"], options={"y_columns": pk.events.data["columns"]})
    ])
  ])

  return page


if __name__ == "__main__":
  from flask import Flask, jsonify, request

  @app.route('/')
  def ui():
    return create_page().outs.html()

  @app.route('/data', methods=['POST'])
  def get_data():
    data = request.get_json()
    columns = ["Trend"] if data["toggle"] else ["Share"]
    return jsonify({"chart_data": sorted(mocks.popularity_2020, key=lambda k: k['Language']), "columns": columns})

  Flask.run(app, host=SERVER_SOCKET_HOST, port=SERVER_SOCKET_PORT, debug=True)
