
from epyk.core.Page import Report
from epyk.core.js import std
from epyk.core.css.themes import ThemeBlue


# Create a basic report object
page = Report()
page.headers.dev()
page.theme = ThemeBlue.BlueGrey()
page.body.add_template(defined_style="doc")

page.ui.title("JavaScript - New Event Name")

h = page.ui.texts.highlights(
  "This illustrates how to add new event names to a page to then be triggered",
  icon="fab fa-js", type="info", options={"close": False})
h.style.css.background = "#f0db4f"

div = page.ui.div("Test")
div.onReady([
  # Create a bespoke type of event
  div.dom.addEventListener("build", std.alert("Ok"))
])

div2 = page.ui.div("Trigger Event")
div2.click([
  # Define the event
  std.createEvent('test_event'),
  std.initEvent("build", 'test_event', True, True),

  # Dispatch this event to trigger the component div
  div2.dom.dispatchEvent(std.getEvent('test_event'))
])

page.ui.layouts.hr()
page.ui.titles.subtitle("Report powered by")
page.ui.rich.powered()


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()


