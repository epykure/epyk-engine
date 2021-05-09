
import epyk as pk


page = pk.Page()
page.headers.dev()

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

c = page.ui.charts.plotly.number_with_delta(45)
#c.label(0, "Test")

page.ui.button("reset").click([
  c.build(90) #dataPoints2),
  #c.js.render(),
])

#c.click([
#  page.js.console.log(c.js.content)
#])

dataPoints3 = [
  {'label': "mango", 'x': 0, 'y': 20, 'y1': 20, 'r': 10},
  {'label': "grape", 'x': 1, 'y': 18, 'y2': 20, 'r': 5}
]

page.ui.button("reset").click([
  c.build(10, options={"delta": {"reference": 0}}),
  #c.js.render(),
])

