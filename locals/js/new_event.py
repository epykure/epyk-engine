
import epyk as pk


# Create a basic report object
page = pk.Page()
page.headers.dev()
page.theme = pk.themes.ThemeBlue.BlueGrey()

page.ui.title("JavaScript - New Event Name")

h = page.ui.texts.highlights(
  "This illustrates how to add new event names to a page to then be triggered",
  icon="fab fa-js", type="info", options={"close": False})
h.style.css.background = "#f0db4f"

div = page.ui.div("Test")
div.onReady([
  # Create a bespoke type of event
  div.dom.addEventListener("build", pk.js_std.alert("Ok"))
])

div2 = page.ui.div("Trigger Event")
div2.click([
  # Define the event
  pk.js_std.createEvent('test_event'),
  pk.js_std.initEvent("build", 'test_event', True, True),

  # Dispatch this event to trigger the component div
  div2.dom.dispatchEvent(pk.js_std.getEvent('test_event'))
])


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()


