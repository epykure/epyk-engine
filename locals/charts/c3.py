
import epyk as pk
import __init__


# Test module to get test data
from epyk.tests import data_urls
from epyk.tests import mocks


# Create a basic report object
page = pk.Page()
page.headers.dev() # Change the Epyk logo
page.body.set_background()
__init__.add_banner(page, __file__)

data = mocks.getSeries(5, 40)

data_rest = page.py.requests.csv(data_urls.PLOTLY_APPLE_PRICES)

ts = page.ui.charts.c3.timeseries(data_rest, y_columns=['AAPL.Open'], x_axis="Date")

g = page.ui.charts.c3.gauge(60)
p = page.ui.charts.c3.pie(data, y_columns=[1], x_axis='g')


d = page.ui.charts.c3.donut(data, y_columns=[1], x_axis='g')
s = page.ui.charts.c3.scatter(data, y_columns=list(range(4)), x_axis='x')

bt = page.ui.button("Click").click([
  s.js.transform('bar'),
  s.d3
])

#stanford = page.ui.charts.c3.stanford(data, y_columns=list(range(4)), x_axis='x', epoch_col=0)

spline = page.ui.charts.c3.spline(data, y_columns=list(range(4)), x_axis='x')
step = page.ui.charts.c3.step(data, y_columns=list(range(4)), x_axis='x')
area = page.ui.charts.c3.area(data, y_columns=list(range(4)), x_axis='x')
area_step = page.ui.charts.c3.area_step(data, y_columns=list(range(4)), x_axis='x')

# a.axis.x.type = 'categorized'
# a.data.names = {'y': 'toto', 'z': 'test'}
# a.data.types = {'y': 'bar'}
# a.data.selection.multiple = True
# a.axis.rotated = True
# a.axis.x.show = False
# #a.point.show = False
# a.point.focus = 200
# a.point.select = 200

b = page.ui.charts.c3.bar(data, y_columns=list(range(4)), x_axis='x')
h = page.ui.charts.c3.hbar(data, y_columns=list(range(4)), x_axis='g')

box = page.ui.div()
box.extend([[g, spline]])
box.extend([[d, p]])
box.add(bt)
box.extend([s, ts, step])
box.extend([b, h, area, area_step])
box.style.configs.doc()

__init__.add_powered(page)

