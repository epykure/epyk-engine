
import epyk as pk


page = pk.Page()

but = page.ui.button("Update Options")
but_title = page.ui.button("Change Title")
but_series = page.ui.button("Update Series")

input = page.ui.input()
text = page.ui.input()
type_chart = page.ui.input("bar")

chart = page.ui.charts.apex.bar()
chart.options.chart.sparkline.enabled = True
chart.options.title.text = "$235,312"
chart.options.subtitle.text = "Expenses"
chart.options.dataLabels.enabled = False
#chart.options.fill.opacity = 0.3
#chart.options.title.text = "Test"

label = page.ui.input()

but_title.click([
  chart.js.updateOptions({"title": {"text": label.dom.content}})
])

#chart.options.plotOptions.radialBar.hollow.size = '70%'
# chart.options.legend.show = True
# chart.options.legend.floating = True
# chart.options.legend.position = "left"

# chart.options.plotOptions.radialBar.endAngle = 270
# chart.options.plotOptions.radialBar.startAngle = 0
# chart.options.plotOptions.radialBar.offsetY = 0
# chart.options.plotOptions.dataLabels.name.fontSize = 30
# chart.options.plotOptions.dataLabels.value.fontSize = 30
# chart.options.plotOptions.dataLabels.total.show = True
# chart.options.plotOptions.dataLabels.total.label = "Total"

chart.options.chart.zoom.custom_config("enabled", False)

#chart.options.chart.stacked = True
#chart.options.yaxis.reversed = True
#chart.options.chart.stackType = "100%"
#chart.options.plotOptions.bar.barHeight = "60%"

# For pie charts
# chart.options.series = [13, 56, 34, 89]
# chart.options.labels = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']

# series = chart.options.add_series()
# series.name = "toto"
# series.data = [{"x": "Test", "y": 45}, {"x": "Test 3", "y": 25}, {"x": "Test 2", "y": 35}, {
#                 "x": 'Kolkata',
#                 "y": 149
#               },]

series = chart.options.add_series()
series.name = "toto2"
series.data = [45, 23, 87, 5]

but.click([
  #line.build(options={"chart": {"type": type_chart.dom.content}})
  chart.js.updateOptions({"chart": {"type": type_chart.dom.content}})
])

but_series.click([
  chart.js.addPointAnnotation({"x": 2, "y": input.dom.content, "label": {"text": text.dom.content}}),
  chart.js.appendSeries({"name": 'newSeries', 'data': [23, 45, 23]}),
  chart.js.appendData([{'data': {}}, {"name": "toto2", 'data': [32, 44, 31, 41, 22]}])
])


