
from epyk.core.Page import Report
from epyk.core.js import std
from epyk.core.css.themes import ThemeBlue


# Create a basic report object
page = Report()
page.headers.dev()
page.theme = ThemeBlue.BlueGrey()
page.body.add_template(defined_style="doc")

page.ui.components_skin = {
  "title": {"css": {"color": "#A89A37"}},
  "layouts.hr": {"css": {"background-color": "#f0db4f", "margin-bottom": "10px"}},
  "button": {"css": {"background": "#323330", "color": "#f0db4f", "border-color": "#323330"}}}

page.ui.title("JavaScript Events")

h = page.ui.texts.highlights('''
This illustrates how to add bespoke JavaScript event to components.
All standard events are mapped and available.
''', icon="fab fa-js", type="info", options={"close": False})
h.style.css.background = "#f0db4f"
page.ui.layouts.hr()

# Add a title to the report
page.ui.title("Events on the page", level=3)

# Trigger a function when a key is pressed on the page
page.ui.text("Press enter to display hello World")

# Add key up event to the page itself
page.js.keyup.enter(std.alert('Hello World'), profile=True)

# Add a title to the report
page.ui.title("Events on a component", level=3)

button = page.ui.button("Click")
button.click([
  page.js.window.setTimeout([
    page.js.console.log("JavaScript triggered after 2 seconds")
  ], 2000, profile={"name": "timeOut"})
], profile={"name": "Click"})

page.ui.layouts.hr()
page.ui.titles.subtitle("Report powered by")
page.ui.rich.powered()


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()

