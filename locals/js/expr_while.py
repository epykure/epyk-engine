
import epyk as pk


# Create a basic report object
page = pk.Page()
page.headers.dev()
page.theme = pk.themes.ThemeBlue.BlueGrey()

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

while_loop = pk.js_expr.whileOf(input, options={"var": 'y'})
input.enter([
  c.dom.write("Common for While"),
  pk.js_std.var('ter', input.dom.content.number),
  pk.js_expr.while_(pk.js_std.var('ter') < 10).fncs([
    c.dom.write(pk.js_std.var("ter"))
  ]).next(pk.js_std.var('ter') + 1),
  c.dom.write("While loop on object items"),
  while_loop.fncs([
    c.dom.write(while_loop.value)
  ]),
])


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()
