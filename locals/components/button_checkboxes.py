
from epyk.core.Page import Report


# Defaults_css.Font.size = 20
# Create a basic report object
page = Report()
page.headers.dev()

data = [
  {"value": "Test 1", "checked": True, "name": 'name'},
  {"value": "Test 2", "dsc": 'description'},
]

# Add a checkbox group
cb2 = page.ui.buttons.checkboxes(data, color="red", width=(100, "px"))
cb2.style.configs.shadow()

# Add a checkbox group with a click event on the items
# The click will display the value of the clicked items in the browser logs
cb = page.ui.buttons.checkboxes(data)
cb.click([page.js.console.log(cb.dom.current)])

# Add some buttons to simulated events.
b = page.ui.button("Add")
d = page.ui.button("Delete")
e = page.ui.button("Empty")
c = page.ui.button("Check")
s = page.ui.button("Style")

# Define the click events on the buttons
b.click([cb.dom.add([{"value": "test"}])])
d.click([cb.dom.delete("test")])
e.click([cb.dom.empty()])
c.click([cb.dom.check("test")])
s.click([cb.dom.css_label("test", {"color": 'orange'})])