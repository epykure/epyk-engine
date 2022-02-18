
import epyk as pk

from epyk.mocks import urls as data_urls


# Create a basic report object
page = pk.Page()
page.headers.dev()

# Add a title to the report
page.ui.title("Panel", level=3)

# Create a basic panel
title = page.ui.title("Title")
slider = page.ui.slider()
paragraph = page.ui.texts.paragraph("This is a paragraph")
panel = page.ui.layouts.panel([title, slider, paragraph])

# Change the style of the panel
panel.style.css.border = "1px solid grey"
panel.style.css.border_radius = "10px"
panel.style.css.padding = 10

# timer for color change onclick

# Add a title to the report
page.ui.title("Sliding Panel", level=3)

# Create a sliding panel
paragraph2 = page.ui.texts.paragraph("This is a paragraph")
sliding = page.ui.panels.sliding([paragraph2], title="Title")
sliding.options.expanded = False

# Add extra HTML component to the sliding panel
paragraph3 = page.ui.texts.paragraph("This is a paragraph 3")
sliding += paragraph3

# Add event on click on the sliding panel title bar
sliding.click([
  page.js.console.log("This is a log")
])

# Add a title to the report
page.ui.title("Split Panels", level=3)

# Create a split panel
left = page.ui.col([
  page.ui.div("left panel"),
  page.ui.date(),
  page.ui.fields.input(),
])

# Get data from a REST API
data_rest_1 = page.py.requests.csv(data_urls.DC_QUAKES)
right = page.ui.col([
  page.ui.div("right panel"),
  page.ui.tables.d3.table(data_rest_1)
])

panel2 = page.ui.panels.split(left, right)

# Add a title to the report
page.ui.title("Drawers Panel", level=3)
# http://jsfiddle.net/KUCaL/

