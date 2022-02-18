
import epyk as pk


page = pk.Page()
page.headers.dev() # Change the Epyk logo

dataPoints = [
  {'x': 0, 'y': 10, 'y1': 10},
  {'x': 1, 'y': 35, 'y1': 20},
  {'x': 2, 'y': 25, 'y1': 10},
  {'x': 3, 'y': 30, 'y1': 5},
  {'x': 4, 'y': 28, 'y1': 10}]

dataPoints2 = [
  {'label': "mango", 'x': 0, 'y': 30, 'y1': 10},
  {'label': "grape", 'x': 1, 'y': 28, 'y1': 5}
]

page.ui.input("Test")

#js_data_object = page.data.js.record(data=dataPoints2)

c = page.ui.charts.c3.line(dataPoints2, y_columns=["y", 'y1'], x_axis='x') #dataPoints, y_columns=["y", 'y1'], x_axis='x')


#
# page.ui.button("reset").click([
#   c.build(dataPoints2),
#   #c.js.render(),
# ])
# #
# c.click([
#   page.js.console.log(c.js.content),
# ])
#
# dataPoints3 = [
#   {'label': "mango", 'x': 0, 'y': 20, 'y1': 20, 'r': 10},
#   {'label': "grape", 'x': 1, 'y': 18, 'y2': 20, 'r': 5}
# ]
#
# page.ui.button("add").click([
#   c.js.load(['test', 1, 15, 26, 89]),
#   #c.js.render(),
# ])
#
# page.ui.button("remove").click([
#   c.js.unload(['test']),
#   #c.js.render(),
# ])
#
#
# page.ui.button("reset").click([
#   c.build(dataPoints3),
#   #c.js.render(),
# ])

