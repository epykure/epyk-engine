
import epyk as pk


# Test module to get test data
from epyk.mocks import urls as data_urls
from epyk.mocks import randoms


# Create a basic report object
page = pk.Page()
page.headers.dev()
page.body.set_background()

# Input data
data = randoms.getSeries(5, 40)
data_rest = page.py.requests.csv(data_urls.PLOTLY_APPLE_PRICES)

scatter = page.ui.charts.nvd3.scatter(data, y_columns=[1, 2, 3, 4], x_axis='x')
scatter.dom.showYAxis(False).showXAxis(False)

records = [
    {'name': 'scripts',
     'children': [
        {"name": "javascript", "size": 10},
        {"name": "python", "size": 5},
        {"name": "ruby", "size": 5},
        {"name": "r", "size": 5}]},
     {"name": "code",
      "children": [
        {"name": "C#", "size": 10},
        {"name": "Java", "size": 5},
      ]
      }
  ]

force = page.ui.charts.nvd3.forceDirected()
force.add_trace({
    "nodes": [
      {"name": "Myriel", "group":1},
      {"name": "Napoleon", "group":1},
      {"name": "Mlle.Baptistine", "group": 5}],
    "links": [
      {"source": 1, "target": 2, "value": 1}
    ]
})

sunburst = page.ui.charts.nvd3.sunburst(records, name='languages')
sc = page.ui.charts.nvd3.candlestick(data_rest, closes=["AAPL.Close"], highs=["AAPL.High"], lows=["AAPL.Low"], opens=["AAPL.Open"], x_axis='Date')
ohlc = page.ui.charts.nvd3.ohlc(data_rest, closes=["AAPL.Close"], highs=["AAPL.High"], lows=["AAPL.Low"], opens=["AAPL.Open"], x_axis='Date')

plot_box = page.ui.charts.nvd3.group_box()
plot_box.add_box(q1=1.05, q3=2.7, mean=3.365, median=1.3, minRegularValue=0.4, maxRegularValue=4.4, minOutlier=0.4, maxOutlier=6)
plot_box.add_box(q1=1.05, q3=2.849999996, mean=3.4949999, median=1.5, minRegularValue=0.3, maxRegularValue=4.9, minOutlier=0.3, maxOutlier=4.9)


multi = page.ui.charts.nvd3.multi(data, y_columns=[1, 2], x_axis='x')
histo = page.ui.charts.nvd3.histo(data, y_columns=[1, 2], x_axis='x')
area = page.ui.charts.nvd3.area(data, y_columns=[3, 4], x_axis='x')

bar = page.ui.charts.nvd3.bar(data, y_columns=[1], x_axis='x')
multibar = page.ui.charts.nvd3.bar(data, y_columns=[1, 2, 3, 4], x_axis='x')
hbar = page.ui.charts.nvd3.hbar(data, y_columns=[1, 2, 3, 4], x_axis='g')

line = page.ui.charts.nvd3.line(data, y_columns=[1, 2, 3, 4], x_axis='x')
cumul = page.ui.charts.nvd3.line_cumulative(data, y_columns=[1, 2, 3, 4], x_axis='x')
line_focus = page.ui.charts.nvd3.line_focus(data, y_columns=[1, 2, 3, 4], x_axis='x')
parallel_coordinates = page.ui.charts.nvd3.parallel_coordinates(data, dimensions=[1, 2, 3, 4])
parallel_coordinates.dom.lineTension(.2)

pie = page.ui.charts.nvd3.pie(data, y_columns=[1], x_axis='g')
donut = page.ui.charts.nvd3.donut(data, y_columns=[1], x_axis='g')
donut_s = page.ui.charts.nvd3.donut(data, y_columns=[1], x_axis='g')
donut_s.dom.padAngle(.08).cornerRadius(5)

#
# page.body.style.custom_class(css_attrs={"_attrs": {"fill": 'red'}}, classname='nvd3.nv-pie .nv-pie-title')
# #page.body.style.add_custom_class(css_attrs={"_attrs": {"fill": 'red'}}, classname='nvd3.nv-pie .nv-pie-title')
#
# toto = page.ui.text("toto")
# toto.style.add_custom_class("super", {"_attrs": {"color": 'red'}})

gauge = page.ui.charts.nvd3.gauge(value=8, text="", total=10)

page.ui.grid([
  [ohlc, force, plot_box],
  [sc, sunburst, parallel_coordinates],
  [bar, multibar, hbar],
  [scatter, gauge],
  [multi, histo, area],
  [line, cumul, line_focus],
  [pie, donut, donut_s]
])


