
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

data_chart = [
  {1: 10, 'x': 4}
]

button = page.ui.button("test")
scatter = page.ui.charts.chartJs.bubble(data_chart, y_columns=[1], x_axis="x")
bar = page.ui.charts.chartJs.bar(data_chart, y_columns=[1], x_axis="x")
pie = page.ui.charts.chartJs.polar(data_chart, y_columns=[1], x_axis="x")
button.click([
  page.js.post("/data_chartjs").onSuccess([
      scatter.build(page.js.objects.data['scatter']),
      pie.build(page.js.objects.data['pie']),
      bar.build(page.js.objects.data['bar'])
  ]),
])
