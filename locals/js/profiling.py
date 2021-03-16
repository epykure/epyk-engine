
from epyk.core.Page import Report
from epyk.core.js import std
from epyk.core.css.themes import ThemeBlue


# Create a basic report object
page = Report()
page.headers.dev()
page.theme = ThemeBlue.BlueGrey()
page.body.add_template(defined_style="doc")

# set the profile for all the JavaScript events
page.profile = True

page.ui.title("JavaScript - Profiling")

h = page.ui.texts.highlights(
  "This illustrates how to use the profile argument to get logs or performances in the browser console",
  icon="fab fa-js", type="info", options={"close": False})
h.style.css.background = "#f0db4f"

# Add a title to the report
page.ui.title("Events on the page", level=3)

# Trigger a function when a key is pressed on the page
page.ui.text("Press enter to display hello World")

# Add key up event to the page itself
page.js.keyup.enter(std.alert('Hello World'))

# Add a title to the report
title = page.ui.title("Click Me !", level=3)
title.click([
  page.js.console.log("title clicked")
])

button = page.ui.button("Click")
button.click([
  page.js.window.setTimeout([
    page.js.console.log("JavaScript triggered after 2 seconds")
  ], 2000)
], profile=False)

page.ui.layouts.hr()
page.ui.titles.subtitle("Report powered by")
page.ui.rich.powered()


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()
