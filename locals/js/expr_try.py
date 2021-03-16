
from epyk.core.Page import Report

from epyk.core.js import expr
from epyk.core.js import std
from epyk.core.css.themes import ThemeBlue


# Create a basic report object
page = Report()
page.headers.dev()
page.theme = ThemeBlue.BlueGrey()
page.body.add_template(defined_style="doc")


page.ui.title("JavaScript Try / Except statement")

h = page.ui.texts.highlights(
  "This illustrates how to add try / except statement from Python",
  icon="fab fa-js", type="info", options={"close": False})
h.style.css.background = "#f0db4f"

input = page.ui.input()

# Simple try except example
input.enter([
  expr
    .try_(input.dom.content.number.toPrecision(500))
    .catch([std.console.log("Error raised precision too large")
  ])
])


input2 = page.ui.input()
input2.enter([
  # Alway raise an exception
  expr.throw("Error! Error!")
])


page.ui.layouts.hr()
page.ui.titles.subtitle("Report powered by")
page.ui.rich.powered()


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()
