
import epyk as pk


# Create a basic report object
page = pk.Page()
page.headers.dev()

page.ui.charts.d3.cloud("This sn example of text in the world cloud")
page.ui.charts.d3.cloud("This is a second example ")

