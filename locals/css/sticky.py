
import epyk as pk

NAME = "Sticky & Anchor"
# Create a basic report object
page = pk.Page()

title = page.ui.title(NAME)

h = page.ui.texts.highlights('''
This will illustrate how to:
- Change a style based on a anchor component.

*scroll down to see the change on the button*
''', icon="fab fa-css3-alt", type="info", color="white", options={"close": False, "markdown": True})
h.style.css.background = "#4C6EF5"
page.ui.layouts.hr()

page.properties.css.add_text('''
.MyColor {position: fixed; bottom: 5px}
''')

page.body.style.css.height = 2000

b = page.ui.button("Sticky text")
b.style.css.color = "green"
b.style.css.bold()

page.body.scroll([
  page.js.if_(title.dom.isInViewPort, [
    b.dom.classList.remove("MyColor")
  ]).else_([
    b.dom.classList.add("MyColor")
  ])
])


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()
