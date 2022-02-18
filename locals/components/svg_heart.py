
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

c = page.ui.charts.svg.heart(w=100, h=200, fill="pink")
c[0].transform("transform", "rotate", "0 100 10", "360 100 100")
c.text("Heart", 50, 100)
