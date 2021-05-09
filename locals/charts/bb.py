
import epyk as pk
import __init__


# Test module to get test data
from epyk.tests import data_urls
from epyk.tests import mocks


# Create a basic report object
page = pk.Page()
page.headers.dev() # Change the Epyk logo
__init__.add_banner(page, __file__)
page.body.set_background()

# Input data
data = mocks.getSeries(5, 40)
data_rest = page.py.requests.csv(data_urls.PLOTLY_APPLE_PRICES)

ts = page.ui.charts.billboard.timeseries(data_rest, y_columns=['AAPL.Open'], x_axis="Date")

g = page.ui.charts.billboard.gauge(60)
p = page.ui.charts.billboard.pie(data, y_columns=[1], x_axis='g')
d = page.ui.charts.billboard.donut(data, y_columns=[1], x_axis='g')
s = page.ui.charts.billboard.scatter(data, y_columns=list(range(4)), x_axis='x')
a = page.ui.charts.billboard.line(data, y_columns=list(range(4)), x_axis='x')

r = page.ui.charts.billboard.line_range(data, y_columns=list(range(4)), x_axis='x')

bubble = page.ui.charts.billboard.bubble(data, y_columns=list(range(4)), x_axis='x')
radar = page.ui.charts.billboard.radar(data, y_columns=list(range(4)), x_axis='g')

spline = page.ui.charts.billboard.spline(data, y_columns=list(range(4)), x_axis='x')
step = page.ui.charts.billboard.step(data, y_columns=list(range(4)), x_axis='x')
area = page.ui.charts.billboard.area(data, y_columns=list(range(4)), x_axis='x')
area_step = page.ui.charts.billboard.area_step(data, y_columns=list(range(4)), x_axis='x')

a.options.axis.x.type = 'categorized'
a.options.data.names = {'y': 'toto', 'z': 'test'}
a.options.data.types = {'y': 'bar'}
a.options.data.selection.multiple = True
a.options.axis.rotated = True
a.options.axis.x.show = False
#a.point.show = False
a.options.point.focus = 200
a.options.point.select = 200

b = page.ui.charts.billboard.bar(data, y_columns=list(range(4)), x_axis='x')
h = page.ui.charts.billboard.hbar(data, y_columns=list(range(4)), x_axis='g')

#a.zoom.enabled = True
#a.zoom.type = 'drag'

page.ui.grid([
  [r, step],
  [area, spline, radar],
  [g, p, d, bubble],
  [s, a, ts],
  [b, h, area_step]
])
__init__.add_powered(page)

