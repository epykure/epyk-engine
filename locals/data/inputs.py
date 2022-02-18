
import epyk as pk


# Create a basic report object
page = pk.Page(
  {'test': "this is a text",
   'test2': "this is a div"}
)
page.headers.dev()

page.ui.text(html_code="test")
page.ui.div(html_code="test2")

