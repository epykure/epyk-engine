
import epyk as pk


page = pk.Page()
page.headers.dev()

dataPoints = [
  {'x': 0, 'y': 10, 'y1': 10, 'text': 'ok'},
  {'x': 1, 'y': 35, 'y1': 20, 'text': 'ok'},
  {'x': 2, 'y': 25, 'y1': 10, 'text': 'ok'},
  {'x': 3, 'y': 30, 'y1': 5, 'text': 'ok'},
  {'x': 4, 'y': 28, 'y1': 10, 'text': 'ok'}]

dataPoints2 = [
  {'label': "mango", 'x': 0, 'y': 30, 'y1': 0},
  {'label': "grape", 'x': 1, 'y': 28, 'y1': 0}
]

page.ui.hidden("Test")

c = page.ui.charts.plotly.line(dataPoints, y_columns=["y"], x_axis='x') # , text_column='text')
#c.label(0, "Test")

page.ui.button("reset").click([
  c.build(dataPoints2),
  #c.js.render(),
])

c.click([
  #page.js.console.log(c.js.value)
])

dataPoints3 = [
  {'label': "mango", 'x': 0, 'y': 20, 'y1': 20, 'r': 10},
  {'label': "grape", 'x': 1, 'y': 18, 'y2': 20, 'r': 5}
]

page.ui.button("reset").click([
  c.build(dataPoints3),
  #c.js.render(),
])

page.ui.button("Add Trace").click([
  c.js.addTraces([{"y": [2, 1, 2]}]),
  #c.js.render(),
])

