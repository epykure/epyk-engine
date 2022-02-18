
import epyk as pk

from epyk.core.data import nvd3

page = pk.Page()
page.headers.dev()

dataPoints = [
  {'x': "Series A", 'y': 10, 'y1': 10},
  {'x': "Series B", 'y': 35, 'y1': 20},
  {'x': "Series B", 'y': 25, 'y1': 10},
  {'x': "Series C", 'y': 30, 'y1': 5},
  {'x': "Series A", 'y': 28, 'y1': 10}]

dataPoints2 = [
  {'label': "mango", 'x': "Series A", 'y': 30, 'y1': 0},
  {'label': "grape", 'x': "Series B", 'y': 28, 'y1': 0}
]

c = page.ui.charts.nvd3.pie(dataPoints, y_columns=["y"], x_axis='x')

# c.click([
#   page.js.console.log("event", skip_data_convert=True)
# ])


page.ui.button("Load").click([
  c.build(nvd3.xy(dataPoints2, ["y"], "x")),
])

#c.click([
#  page.js.console.log(c.js.content)
#])

dataPoints3 = [
  {'label': "mango", 'x': 0, 'y': 20, 'y1': 20, 'r': 10},
  {'label': "grape", 'x': 1, 'y': 18, 'y2': 20, 'r': 5}
]

page.ui.button("reset").click([
  c.build(nvd3.xy(dataPoints3, ["y"], "x")),
])

