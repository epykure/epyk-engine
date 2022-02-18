
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

# Add the input text
input = page.ui.input(html_code="test")

# Create the text to be displayed as a popup message temporarily
message = page.ui.texts.note("Some text...", "Success")
message.style.css.display = False
page.ui.button("Click").click([
  message.build(input.dom.content),
  message.dom.show(duration=5)
])
