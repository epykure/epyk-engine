
import epyk as pk
import __init__


# Create a basic report object
page = pk.Page()
page.headers.dev()
__init__.add_banner(page, __file__)

page.ui.charts.sparkline("box", [1, 2, 3, 4, 5, 4, 3, 2, 1])
l = page.ui.charts.sparkline("line", [1, 2, 3, 4, 5, 4, 3, 2, 10])
l.click([
  page.js.console.log(l.dom.val),
  page.js.console.log(l.dom.content),
  page.js.console.log(l.dom.offset),
])

s = page.ui.charts.sparkline("bar", [1, 2, 3], title="Top Clients (#)",  options={"barWidth": 20})
s.hover([
  page.js.console.log(s.dom.val),
  page.js.console.log(s.dom.content),
  page.js.console.log(s.dom.offset),
])

__init__.add_powered(page)
