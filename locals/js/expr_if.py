
from epyk.core.Page import Report
from epyk.core.js import expr
from epyk.core.css.themes import ThemeBlue


# Create a basic report object
page = Report()
page.headers.dev()
page.theme = ThemeBlue.BlueGrey()
page.body.add_template(defined_style="doc")


page.ui.title("JavaScript If statement")

h = page.ui.texts.highlights(
  "This illustrates how to add if statement in the JavaScript entry points in the framework and easily deal inputs",
  icon="fab fa-js", type="info", options={"close": False})
h.style.css.background = "#f0db4f"


page.ui.titles.subtitle("Is the number above 10?")
input = page.ui.input(placeholder="Put a number")

# Just generate a simple if statement on the value of the input
button = page.ui.button("Check").click([
  expr
    .if_(input.dom.content.number > 10, [page.js.alert("Yes it is!")])
    .elif_(input.dom.content.number > 5, [page.js.alert("Not really but close")])
    .else_([page.js.alert("No")
  ])
])
button.style.css.background = "#323330"
button.style.css.color = "#f0db4f"
button.style.css.border_color = "#323330"

page.ui.layouts.hr()
page.ui.titles.subtitle("Report powered by")
page.ui.rich.powered()


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()

