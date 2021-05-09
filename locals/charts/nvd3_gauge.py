
import epyk as pk
import __init__

page = pk.Page()
page.headers.dev()
__init__.add_banner(page, __file__)

c = page.ui.charts.nvd3.gauge(42)

page.ui.button("reset").click([
  c.build(40),
])


dataPoints3 = [
  {'label': "mango", 'x': 0, 'y': 20, 'y1': 20, 'r': 10},
  {'label': "grape", 'x': 1, 'y': 18, 'y2': 20, 'r': 5}
]

page.ui.button("reset").click([
  c.build(90),
])
__init__.add_powered(page)

