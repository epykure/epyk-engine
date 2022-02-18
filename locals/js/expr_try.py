
import epyk as pk


# Create a basic report object
page = pk.Page()
page.headers.dev()
page.theme = pk.themes.ThemeBlue.BlueGrey()

page.ui.title("JavaScript Try / Except statement")

h = page.ui.texts.highlights(
  "This illustrates how to add try / except statement from Python",
  icon="fab fa-js", type="info", options={"close": False})
h.style.css.background = "#f0db4f"

input = page.ui.input()

# Simple try except example
input.enter([
  pk.js_expr
    .try_(input.dom.content.number.toPrecision(500))
    .catch([pk.js_std.console.log("Error raised precision too large")
  ])
])


input2 = page.ui.input()
input2.enter([
  # Always raise an exception
  pk.js_expr.throw("Error! Error!")
])


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()
