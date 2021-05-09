
import epyk as pk
import __init__


# Test module to get test data
from epyk.tests import data_urls


page = pk.Page()
page.headers.dev()
__init__.add_banner(page, __file__)

data = page.py.requests.csv(data_urls.PLOTLY_POINTS)

c = page.ui._2d.vis.bar(data, y_columns=["y"], x_axis="x")

page.ui.button("reset").click([
  c.build(page.data.vis.xy(data[:6], y_columns=["x"], x_axis="x")),
  page.js.console.log(c.js.getDataRange())
])
__init__.add_powered(page)

