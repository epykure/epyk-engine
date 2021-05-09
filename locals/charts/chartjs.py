
import epyk as pk


# Test module to get test data
from epyk.tests import data_urls
from epyk.tests import mocks


# Create a basic report object
page = pk.Page()
page.headers.dev() # Change the Epyk logo
page.body.set_background()

# Input data
data = mocks.getSeries(5, 30)
data_rest = page.py.requests.csv(data_urls.PLOTLY_APPLE_PRICES)

ts = page.ui.charts.chartJs.timeseries(data_rest, y_columns=['AAPL.Open'], x_axis="Date")

yaxis = ts.options.scales.add_y_axis()
yaxis.gridLines.display = True
yaxis.gridLines.color = 'red'
yaxis.gridLines.zeroLineWidth = 1
yaxis.gridLines.zeroLineColor = 'red'
yaxis.gridLines.drawBorder = True
yaxis.ticks.fontColor = 'red'
yaxis.ticks.beginAtZero = True
yaxis.add_label('Y Axis', color='white')

xaxis = ts.options.scales.x_axes()
xaxis.ticks.fontColor = 'white'
xaxis.display = False
ts.options.legend.labels.fontColor = 'white'

a = page.ui.charts.chartJs.line(data, y_columns=[3, 4], x_axis='x')


donut = page.ui.charts.chartJs.donut(data[:5], y_columns=[2], x_axis='x')
p = page.ui.charts.chartJs.pie(data[:5], y_columns=[2], x_axis='x')
p.dataset().hoverBorderWidth = 10
p.click([
  p.js.reset()
])

page.ui.button("Click").click([
  p.js.update(),

])

r = page.ui.charts.chartJs.radar(data[:5], y_columns=[2, 3, 4], x_axis='x')
r.options.legend.labels.fontColor = 'white'
r.click([
  page.js.alert("event", skip_data_convert=True)
])
polar = page.ui.charts.chartJs.polar(data[:5], y_columns=[1], x_axis='x')
polar.options.add_title("Title", color="red")
#polar.click([
#  page.js.console.log(polar.js.value)
#])
polar.options.legend.labels.fontColor = 'white'
for d in polar.datasets:
  d.borderWidth = 0

li = page.ui.charts.chartJs.line(data, y_columns=list(range(4)), x_axis='x')
l = page.ui.charts.chartJs.step(data, y_columns=list(range(4)), x_axis='x')
l.options.showLines = True
# l.options.scales.y_axis().ticks.max = 5
# l.options.scales.y_axis().ticks.min = 5
#l.options.scales.xAxes.ticks.min = 0

bu = page.ui.charts.chartJs.bubble(data, y_columns=list(range(4)), x_axis='x', r_values=['r'])
bu.click([
  page.js.console.log(bu.js.value)
])

s = page.ui.charts.chartJs.scatter(data, y_columns=list(range(4)), x_axis='x')
s.click([
  page.js.console.log(s.js.value)
])

h = page.ui.charts.chartJs.hbar(data[:5], y_columns=list(range(4)), x_axis='x')
h.click([
  page.js.console.log(h.js.value)
])

#b = page.ui.charts.chartJs.bar(data, y_columns=[1, 2, 3], x_axis='x')
# b.add_dataset([2, 3, 4, 5, 6])

page.ui.grid([
  [ts, r, li, polar],
#  [bu, b, h, a],
  [p, l, s, donut]
])

page.ui.button("test").click([

])

page.ui.tables.tabulators.table()
