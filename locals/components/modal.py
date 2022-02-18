

from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

input = page.ui.input(html_code="test")

message = page.ui.texts.note("Some text...", "Success", width=(250, 'px'))
message.style.css.position = 'fixed'
message.style.css.bottom = 10
message.style.css.right = 10

message.style.css.display = False
page.ui.button("Click").click([
  message.build(input.dom.content),
  message.dom.show(duration=2)
])