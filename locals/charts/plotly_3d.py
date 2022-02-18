
import epyk as pk


# Test module to get test data
from epyk.mocks import urls as data_urls


page = pk.Page()
page.headers.dev()

dataPoints = [
  {'x': 0, 'y': 10, 'y1': 10},
  {'x': 1, 'y': 35, 'y1': 20},
  {'x': 2, 'y': 25, 'y1': 10},
  {'x': 3, 'y': 30, 'y1': 5},
  {'x': 4, 'y': 28, 'y1': 10}]

dataPoints2 = [
  {'label': "mango", 'x1': 0, 'y1': 30, 'z1': 0},
  {'label': "grape", 'x1': 1, 'y1': 28, 'z1': 0}
]

page.ui.hidden("Test")


data_rest = page.py.requests.csv(data_urls.PLOTLY_3D)

c1 = page.ui._3d.plotly.ribbon(data_rest, y_columns=["y1"], x_axis='x1', z_axis="z1")
c2 = page.ui._3d.plotly.surface(data_rest, y_columns=["y2"], x_axis='x2', z_axis="z2")

page.ui.row([c1, c2])

page.ui.button("reset 1").click([
  c1.build(dataPoints2),
  #c.js.render(),
])

c1.click([
  #page.js.console.log(c.js.value)
])

dataPoints3 = [
  {'label': "mango", 'x': 0, 'y': 20, 'y1': 20, 'r': 10},
  {'label': "grape", 'x': 1, 'y': 18, 'y2': 20, 'r': 5}
]


page.ui.button("reset 2").click([
  c2.build(page.data.plotly.surface(data_rest, y_columns=["y1"], x_axis="x1", z_axis="z1")),
  #c.js.render(),
])

