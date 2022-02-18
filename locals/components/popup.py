#error
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

div = page.ui.div("Test")
div.style.css.background = 'white'

button = page.ui.button("show")
popup = page.ui.layouts.popup([div], options={"background": False, 'draggable': True})

button.click([
  popup.dom.show()
])

