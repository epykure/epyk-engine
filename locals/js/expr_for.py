
from epyk.core.Page import Report
from epyk.core.js import expr
from epyk.core.js import std
from epyk.core.css.themes import ThemeBlue

# Create a basic report object
page = Report()
page.headers.dev()
page.theme = ThemeBlue.BlueGrey()
page.body.add_template(defined_style="doc")


page.ui.title("JavaScript For statement")

h = page.ui.texts.highlights(
  "This illustrates how to add For statement in the JavaScript entry points in the framework and easily deal inputs",
  icon="fab fa-js", type="info", options={"close": False})
h.style.css.background = "#f0db4f"

input = page.ui.input(placeholder="Put a number")

c = page.ui.rich.console(
  "* This is a log section for all the events in the different buttons *", options={"timestamp": True})

input.enter([
  c.dom.write("Common for loop"),
  expr.for_(input).fncs([
    c.dom.write(std.var("i"))
  ]),

  c.dom.write("For loop on object properties"),
  expr.forIn(input).fncs([
    std.console.log(std.var("x"))
  ]),

c.dom.write("For loop on object items"),
  expr.forOf(input, options={"var": 'y'}).fncs([
    c.dom.write(std.var("y"))
  ]),
])

page.ui.layouts.hr()
page.ui.titles.subtitle("Report powered by")
page.ui.rich.powered()


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()
