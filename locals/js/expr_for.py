
import epyk as pk


# Create a basic report object
page = pk.Page()
page.headers.dev()
page.theme = pk.themes.ThemeBlue.BlueGrey()

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
  pk.js_expr.for_(input).fncs([
    c.dom.write(pk.js_std.var("i"))
  ]),

  c.dom.write("For loop on object properties"),
  pk.js_expr.forIn(input).fncs([
    pk.js_std.console.log(pk.js_std.var("x"))
  ]),

c.dom.write("For loop on object items"),
  pk.js_expr.forOf(input, options={"var": 'y'}).fncs([
    c.dom.write(pk.js_std.var("y"))
  ]),
])


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()
