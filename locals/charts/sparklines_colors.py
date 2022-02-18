
import epyk as pk


# Create a basic report object
page = pk.Page()
page.headers.dev()

s = page.ui.charts.sparkline("line", [1, 2, 3, 4, 5, 4, 3, 2, 1])
s.color("#FFFF00")

s = page.ui.charts.sparklines.box_plot([1, 2, 3, 4, 5, 4, 3, 2, 1])

