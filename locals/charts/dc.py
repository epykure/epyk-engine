
import epyk as pk


# Test module to get test data
from epyk.tests import mocks


page = pk.Page()
page.headers.dev()
page.body.set_background()

# Create a Javascript Crossfilter object
data = mocks.getSeries(5, 30)
crossfilter = page.js.data.crossfilter(data, "test")
dimension = crossfilter.dimension([('x', int)], 'test_dim')
group = dimension.group('group').reduceSum(1)

# Write the object to the Javascript page
page.body.onLoad([
  crossfilter, dimension, group
])

# Create a DC line chart and add crossfilter definition
line1 = page.ui.charts.dc.line() # data, y_columns=[1, 2], x_axis='x'
line1.crossFilter(dimension, group)

# Create a DC line chart and add crossfilter definition
pie2 = page.ui.charts.dc.pie(height=(150, "px")) # data, y_columns=[1, 2], x_axis='x'
pie2.crossFilter(dimension, group)

# Create a DC line chart and add crossfilter definition
pie3 = page.ui.charts.dc.bar(height=(150, "px")) # data, y_columns=[1, 2], x_axis='x'
pie3.crossFilter(dimension, group)

#
data = mocks.getSeries(5, 30)
line = page.ui.charts.dc.line(data, y_columns=[1, 2], x_axis='x')
step = page.ui.charts.dc.step(data, y_columns=[1, 2], x_axis='x')
bar = page.ui.charts.dc.bar(data, y_columns=[3, 4], x_axis='x')
hbar = page.ui.charts.dc.hbar(data[:10], y_columns=4, x_axis='x')
pie = page.ui.charts.dc.pie(data[:5], y_columns=3, x_axis='x')
scatter = page.ui.charts.dc.scatter(data, y_columns=[2, 4], x_axis='x')
bubble = page.ui.charts.dc.bubble(data, y_columns=3, x_axis='x', r_axis=4, options={'statc_factor': '/10'})

# Report layout
page.ui.title("DC Charts")
page.body.style.css.padding = "0 10px"

# Report grid
page.ui.grid([
  [page.ui.col([
      page.ui.title("DC Line chart", level=4),
      page.ui.text("Example of a "),
      line1
   ]),
   page.ui.col([
     page.ui.title("DC Line chart", level=4),
     page.ui.row([
       page.ui.text("Example of a "),
       pie2
     ]),
     page.ui.row([
       pie3,
       page.ui.text("Example of a ")
     ])
   ])
  ],
  [page.ui.title("Bespoke Examples", level=4).css({"color": 'black'})],
  [line, step, scatter],
  [bar, hbar],
  [bubble, pie],
])

