from epyk.core.Page import Report
from epyk.core.js import expr
from epyk.core.data import events
from epyk.core.data import chartJs
from epyk.core.css.themes import ThemeBlue


# Socket server url
SERVER_SOCKET_HOST = "127.0.0.1"
SERVER_SOCKET_PORT = 5000

import random
from flask import Flask
app = Flask(__name__)


def create_page():
  page = Report()
  page.theme = ThemeBlue.BlueGrey()

  page.body.style.css.background = "linear-gradient(45deg, #00f 1%, #fff 1%, #fff 49%, #00f 49%, #00f 51%, #fff 51%, #fff 99%, #00f 99%)"
  page.body.style.css.background_size = "20px 20px"
  page.body.style.css.background_position = "0 0"
  page.body.style.css.text_align = "center"
  page.body.style.css.padding_top = 10
  page.body.style.css.padding_bottom = 10
  page.body.style.css.min_height = "100%"

  container = page.ui.div(width=(100, '%'), height=(100, '%'))
  container.style.css.background = "white"
  container.style.css.max_width = "600px"
  container.style.css.margin = "auto"
  container.style.css.padding = "0 10px"
  container.style.css.shadow_box()

  title = page.ui.titles.head("Pseudorandom Number Generator in Python")
  title.style.css.display = "inline-block"
  container.add(title)

  sub_title0 = page.ui.titles.title("Mersenne Twister")
  paragraph = page.ui.panels.sliding('''
  The Mersenne Twister is a pseudorandom number generator (PRNG). It is by far the most widely used general-purpose PRNG.[1] Its name derives from the fact that its period length is chosen to be a Mersenne prime.
  
  The Mersenne Twister was developed in 1997 by Makoto Matsumoto [ja] (松本 眞) and Takuji Nishimura (西村 拓士).[2] It was designed specifically to rectify most of the flaws found in older PRNGs.
  
  The most commonly used version of the Mersenne Twister algorithm is based on the Mersenne prime 219937−1. The standard implementation of that, MT19937, uses a 32-bit word length. There is another implementation (with five variants[3]) that uses a 64-bit word length, MT19937-64; it generates a different sequence.
  ''', sub_title0)
  container.add(paragraph)
  container.add(page.ui.layouts.hr())

  sub_title = page.ui.titles.title("Parameters")
  container.add(sub_title)

  seed1 = page.ui.fields.input(label="seed", html_code="seed")
  container.add(seed1)

  n = page.ui.fields.input(label="Samples", html_code="n")
  container.add(n)

  valid = page.ui.buttons.colored("Run Python")
  valid_js = page.ui.buttons.colored("Run Javascript")
  valid_js.style.css.margin_left = 10
  container.add(page.ui.div([valid, valid_js]))
  container.add(page.ui.layouts.hr())
  py_title = page.ui.titles.section("Python Results")
  container.add(py_title)

  line = page.ui.charts.chartJs.line([], y_columns=["y"], x_axis=["x"], height=160)
  bar = page.ui.charts.chartJs.bar([], y_columns=["c"], x_axis=["b"], height=160)
  container.add(page.ui.row([line, bar]).css({"background": 'white'}))

  js_title = page.ui.titles.section("Javascript Results")
  container.add(js_title)
  js_line = page.ui.charts.chartJs.line([], y_columns=["y"], x_axis=["x"], height=160)
  container.add(js_line)

  valid.click([
    page.js.objects.time("window.time_py"),
    page.js.post("/compute", [seed1, n]).onSuccess([
      line.build(events.data["line"]),
      bar.build(events.data["bar"]),
      page.js.console.perf("window.time_py", label="Python Processing: "),
      page.js.print("Python computed", 2000, cssAttrs={"bottom": "10px", 'right': "10px", 'position': 'fixed'})
    ]),
  ])

  valid_js.click([
    page.js.objects.list.new([], "js_data"),
    page.js.objects.time("window.time_py"),
    expr.for_(n, [
      page.js.objects.new({}, "row"),
      page.js.objects.get("row").setattr("y", page.js.math.random()).r,
      page.js.objects.get("row").setattr("x", page.js.objects.get("i")).r,
      page.js.objects.list.get("js_data").push(page.js.objects.get("row"))
    ]),
    js_line.build(page.js.objects.list.get("js_data")),
    page.js.console.perf("window.time_py", label="Javascript Processing: "),
    page.js.print("Javascript computed", 2000, cssAttrs={"bottom": "10px", 'right': "10px", 'position': 'fixed'})
  ])
  return page


if __name__ == "__main__":
  from flask import Flask, jsonify, request

  @app.route('/')
  def ui():
    return create_page().outs.html()

  @app.route('/compute', methods=['POST'])
  def compute():
    data = request.get_json()
    random.seed(int(data["seed"]))
    records = [{"c": 1, "x": i, "y": random.random()}for i in range(int(data["n"]))]
    for r in records:
      r["b"] = round(r["y"], 1)
    return jsonify({"line": chartJs.y(records[:100], ["y"], "x"), "bar": chartJs.y(records, ["c"], "b")})


  Flask.run(app, host=SERVER_SOCKET_HOST, port=SERVER_SOCKET_PORT, debug=True)
