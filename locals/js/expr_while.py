
from epyk.core.Page import Report
from epyk.core.js import expr
from epyk.core.js import std
from epyk.core.css.themes import ThemeBlue


# Create a basic report object
page = Report()
page.headers.dev()
page.theme = ThemeBlue.BlueGrey()
page.body.add_template(defined_style="doc")


page.ui.title("JavaScript While statement")

h = page.ui.texts.highlights(
  "This illustrates how to add while loops from Python",
  icon="fab fa-js", type="info", options={"close": False})
h.style.css.background = "#f0db4f"

input = page.ui.input(placeholder="Put a number and press enter")

# Console component
page.ui.titles.subtitle("Console logs")
c = page.ui.rich.console(
  "* This is a log section for all the events in the different buttons *", options={"timestamp": True})

while_loop = expr.whileOf(input, options={"var": 'y'})
input.enter([
  c.dom.write("Common for While"),
  std.var('ter', input.dom.content.number),
  expr.while_(std.var('ter') < 10).fncs([
    c.dom.write(std.var("ter"))
  ]).next(std.var('ter') + 1),
  c.dom.write("While loop on object items"),
  while_loop.fncs([
    c.dom.write(while_loop.value)
  ]),

])

page.ui.layouts.hr()
page.ui.titles.subtitle("Report powered by")
page.ui.rich.powered()


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()
