
import epyk as pk


# Create a basic report object
page = pk.Page()
page.theme = pk.themes.ThemeBlue.BlueGrey()

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
page.js.keyup.enter(pk.js_std.alert('Hello World'))

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


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()
