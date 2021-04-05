
from epyk.core.Page import Report
from epyk.tests import data_urls
from epyk.core.data import events

import pandas as pd

import sys
import asyncio
import tornado.ioloop
import tornado.web
import tornado.escape


# Socket server url
SERVER_SOCKET_HOST = "127.0.0.1"
SERVER_SOCKET_PORT = 5000

DATA_CACHE = None


class MainHandler(tornado.web.RequestHandler):

  def post(self):
    data = tornado.escape.json_decode(self.request.body)
    result = []
    for rec in DATA_CACHE:
      if data['Year']['input'] <= int(rec["Year"]):
        result.append(rec)
    self.write({"table": result})

  def get(self):
    self.write(create_page().outs.html())


def make_app(debug=True):
  return tornado.web.Application([
    (r"/", MainHandler),
    (r"/data", MainHandler),
  ], debug=debug)


NAMES = {'Entity': 'Entity', 'Year': 'Year', 'Births outside of marriage (% of all births)': 'Births'}


def create_page():
  global DATA_CACHE

  page = Report()
  page.headers.dev()
  DATA_CACHE = page.py.requests.csv(data_urls.OWID_BIRTH_OUT_MARRIAGE, store_location=r"C:\tmps")
  data = pd.DataFrame(DATA_CACHE, columns=['Entity', 'Year', 'Births outside of marriage (% of all births)'])
  data['Births outside of marriage (% of all births)'] = pd.to_numeric(data['Births outside of marriage (% of all births)'])
  mean_per_years = data.groupby(["Year"])["Births outside of marriage (% of all births)"].mean().to_dict()

  template = page.body.add_template(defined_style="doc")
  template.style.css.background = page.theme.greys[0]
  filters, width = [], 80
  for k in DATA_CACHE[0].keys():
    name = NAMES[k]
    filters.append(page.ui.buttons.filter(name, is_number=True, width=(width, 'px'), html_code=name))

  gauge = page.ui.charts.apex.gauge(mean_per_years["2010"], "2010", height=100)
  gauge.colors(["red", "blue"])
  gauge2 = page.ui.charts.apex.gauge(mean_per_years["2011"], "2011", height=100)
  gauge2.colors(["blue"])
  gauge3 = page.ui.charts.apex.gauge(mean_per_years["2012"], "2012", height=100)
  gauge4 = page.ui.charts.apex.gauge(mean_per_years["2013"], "2013", height=100)
  gauge4.colors(["purple"])

  img = page.ui.img("https://img.stackshare.io/service/1002/tornado.png", width=100, height=100)
  img.style.css.fixed(top=(0, "px"), right=(24, "%"))

  page.ui.titles.head("Birth outside marriage trend")
  page.ui.titles.headline("Yearly KPI")
  page.ui.titles.underline(width=100)
  row = page.ui.row([gauge, gauge2, gauge3, gauge4])
  refresh = page.ui.buttons.colored("Update")
  refresh.style.css.margin_top = 10
  filters.append(refresh)
  row.options.responsive = False
  row.options.autoSize = False
  columns = page.ui.div(filters, width=(width, 'px'))
  table = page.ui.table(DATA_CACHE)
  table.style.css.width_calc(110)
  table.style.css.float = "right"
  table.config.paginationSize = 10
  page.ui.titles.headline("Raw data")
  page.ui.titles.underline(width=100)
  container = page.ui.div([columns, table])
  page.ui.texts.references.github(data_urls.OWID_BIRTH_OUT_MARRIAGE)
  container.style.css.display = "inline-block"

  refresh.click([
    page.js.post("/data", components=filters).onSuccess([
      table.build(events.data["table"])
    ]),
    gauge.build(page.js.math.random(1, 100)),
    gauge2.build(page.js.math.random(1, 100)),
    gauge3.build(page.js.math.random(1, 100)),
    gauge4.build(page.js.math.random(1, 100)),
  ])

  page.ui.layouts.hr()
  page.ui.rich.powered()

  return page


if __name__ == "__main__":

    if sys.platform == 'win32' and hasattr(asyncio, 'WindowsSelectorEventLoopPolicy'):
      asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    app = make_app(debug=True)
    app.listen(SERVER_SOCKET_PORT)
    tornado.ioloop.IOLoop.current().start()
