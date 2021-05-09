
import epyk as pk
import __init__


page = pk.Page()
page.headers.dev() # Change the Epyk logo
__init__.add_banner(page, __file__)

dataPoints = [
  {'x': 0, 'y': 10, 'y1': 10},
  {'x': 1, 'y': 35, 'y1': 20},
  {'x': 2, 'y': 25, 'y1': 10},
  {'x': 3, 'y': 30, 'y1': 5},
  {'x': 4, 'y': 28, 'y1': 10}]

dataPoints2 = [
  {'label': "mango", 'x': 0, 'y': 30, 'y1': 0},
  {'label': "grape", 'x': 1, 'y': 28, 'y1': 0}
]

page.ui.hidden("Test")

c = page.ui.charts.billboard.stacked(dataPoints, y_columns=["y", 'y1'], x_axis='x')

page.ui.button("reset").click([
  c.build(dataPoints2),
  #c.js.render(),
])

c.click([
  page.js.console.log(c.js.value),
])

dataPoints3 = [
  {'label': "mango", 'x': 0, 'y': 20, 'y1': 20, 'r': 10},
  {'label': "grape", 'x': 1, 'y': 18, 'y2': 20, 'r': 5}
]

page.ui.button("reset").click([
  c.build(dataPoints3),
  #c.js.render(),
])

__init__.add_powered(page)
