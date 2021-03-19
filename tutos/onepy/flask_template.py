from epyk.core.Page import Report
from epyk.core.data import chartJs
from epyk.core.css.themes import ThemeBlue
from epyk.tests import mocks
from epyk.core.js import std

import requests

# Socket server url
SERVER_SOCKET_HOST = "127.0.0.1"
SERVER_SOCKET_PORT = 5000


from flask import Flask
app = Flask(__name__)


def create_page():
  page = Report()
  page.headers.dev()
  page.body.add_template(defined_style="doc")
  page.theme = ThemeBlue.BlueGrey()

  title = page.ui.title("Python")
  page.ui.layouts.underline()
  title.options.editable = True

  sub_title = page.ui.titles.subtitle("The Python Community")
  page.ui.menu(sub_title, post="/bar")

  p = page.ui.paragraph('''
  The [Python Software Foundation](https://www.python.org/psf/) and the global Python community welcome and encourage 
  participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working 
  to help each other live up to these principles.
  ''', options={"markdown": True})
  page.ui.menu(p)

  table = page.ui.tables.tabulator(mocks.languages)
  page.ui.tables.menu(table, post="/table")

  page.ui.titles.subtitle("Zoom on a package")
  pkg_name = page.ui.fields.input("epyk", label="Package name", html_code="package")

  bar_chart = page.ui.charts.chartJs.bar(y_columns=["download"], x_axis="name")
  menu_bar = page.ui.charts.menu(bar_chart, post={"url": "/chart", "components": [pkg_name]})

  pie_chart = page.ui.charts.chartJs.pie(y_columns=["value"], x_axis="type")
  menu_pie = page.ui.charts.menu(pie_chart, post={"url": "/pie", "components": [pkg_name]})

  row = page.ui.row([[menu_bar, bar_chart], [menu_pie, pie_chart]], position="top")
  row.options.responsive = False
  row.options.autoSize = False

  sub_title2 = page.ui.titles.subtitle("Conferences and Workshops")
  sub_title2.options.editable = True
  p2 = page.ui.paragraph('''
  There are a number of conferences held each year where the Python community gathers together (listed alphabetically):
  ''', options={"markdown": True})
  page.ui.menu(p2, save_funcs=[
    page.js.alert(p2.dom.content)
  ], update_funcs=[
    p2.build("Updated paragraph")
  ], profile=True)

  sq = page.ui.lists.squares([
    "DjangoCon Europe"
  ])
  page.ui.lists.menu(sq)

  page.ui.layouts.hr().css({"margin-top": '20px'})
  page.ui.titles.subtitle("Report powered by")
  page.ui.rich.powered()

  page.ui.icons.fixed("fas fa-file-download").click([
    std.var("backboneData", global_scope=True).addComponent(sub_title),
    page.js.clipboard(std.var("backboneData", global_scope=True).stringify()),
    page.js.window.download(
      page.js.window.btoa(std.var("backboneData", global_scope=True).stringify()), "configuration.json")
    # page.js.location.download(page.js.location.getUrlFromData(std.var("backboneData", global_scope=True).stringify()))
  ])

  page.body.onReady([
    std.var("backboneData", value={}, global_scope=True),
  ])
  return page


if __name__ == "__main__":
  from flask import Flask, jsonify, request

  @app.route('/')
  def ui():
    return create_page().outs.html()


  @app.route('/bar', methods=["POST"])
  def bar():
    return jsonify("Ok")


  @app.route('/bar2', methods=["POST"])
  def bar2():
    return jsonify("Ok 2")


  @app.route('/table', methods=["POST"])
  def table():
    return jsonify([
      {"name": 'Ada'},
      {"name": 'Fortran'},
    ])


  @app.route('/chart', methods=["POST"])
  def chart():
    data = request.get_json()

    results = requests.get("https://pypistats.org/api/packages/%(package)s/recent" % data).json()["data"]
    rec = [
      {"download": results["last_month"], 'name': "last_month"},
      {"download": results["last_day"], 'name': "last_day"},
    ]
    return jsonify(chartJs.y(rec, y_columns=["download"], x_axis='name'))


  @app.route('/pie', methods=["POST"])
  def pie():
    # https://api.stackexchange.com/2.2/questions/unanswered?order=desc&sort=activity&tagged=jquery&site=stackoverflow
    data = request.get_json()
    rec = []
    results = requests.get(
      "https://api.stackexchange.com/2.2/questions/unanswered?order=desc&sort=activity&tagged=%(package)s&site=stackoverflow" % data).json()
    rec.append({"type": 'Not Answered', "value": len(results["items"])})
    results = requests.get(
      "https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&tagged=%(package)s&site=stackoverflow" % data).json()
    rec.append({"type": 'Total', "value": len(results["items"])})
    return jsonify(chartJs.y(rec, y_columns=["value"], x_axis='type'))

  Flask.run(app, host=SERVER_SOCKET_HOST, port=SERVER_SOCKET_PORT, debug=True)
