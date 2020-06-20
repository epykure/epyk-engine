
from epyk.core.Page import Report
from epyk.tests import data_urls


page = Report()
page.headers.dev()

csv = page.js.d3.csv(data_urls.PLOTLY_APPLE_PRICES)

i = page.ui.input()

page.ui.button("click").click([
  csv.filterCol("direction", i.dom.content),
  page.js.console.log(csv.unpack("test", "direction")),
  page.js.console.log(i.dom.content)
])

data_rest_1 = page.py.requests.csv(data_urls.DC_QUAKES)

page.ui.tables.d3.table(data_rest_1)

