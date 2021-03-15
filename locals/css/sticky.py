
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

title = page.ui.title("This is the anchor")
page.properties.css.add_text('''
.MyColor {position: fixed; bottom: 0; left: 0}
''')

h = page.ui.texts.highlights(
  "Scroll down to see the change on the button",
  icon="fas fa-search-plus", type="info", options={"close": False})

container = page.ui.div(height=(2000, 'px'))
b = page.ui.button("Test")
container.extend([title, h, b])
container.style.doc()

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
