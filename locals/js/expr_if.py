
import epyk as pk


# Create a basic report object
page = pk.Page()
page.headers.dev()
page.theme = pk.themes.ThemeBlue.BlueGrey()

page.ui.title("JavaScript If statement")

h = page.ui.texts.highlights(
  "This illustrates how to add if statement in the JavaScript entry points in the framework and easily deal inputs",
  icon="fab fa-js", type="info", options={"close": False})
h.style.css.background = "#f0db4f"


page.ui.titles.subtitle("Is the number above 10?")
input = page.ui.input(placeholder="Put a number")

# Just generate a simple if statement on the value of the input
button = page.ui.button("Check").click([
  pk.js_expr
    .if_(input.dom.content.number > 10, [page.js.alert("Yes it is!")])
    .elif_(input.dom.content.number > 5, [page.js.alert("Not really but close")])
    .else_([page.js.alert("No")
  ])
])
button.style.css.background = "#323330"
button.style.css.color = "#f0db4f"
button.style.css.border_color = "#323330"


