
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

page.ui.charts.svg.arrow_left(y1=40)

svg = page.ui.charts.svg.axes()
m = svg.defs().marker("circle", "0 0 10 10", 5, 5)
m.circle(5, 5, 5, 'red')
m.markerWidth(10).markerHeight(10)
p = svg.path(0, 0, from_origin=True).line_to(50, 100).\
  horizontal_line_to(300).\
  line_to(400, 200).smooth_quadratic_bezier_curve_to(50, 50)
p.markers(m.url)

