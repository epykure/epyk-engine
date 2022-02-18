# error
from epyk.core.Page import Report


page = Report()
page.headers.dev()

# Console component
c = page.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

# Button checkbox
c1 = page.ui.buttons.check(label="C1")

# With some specific CSS Style
c2 = page.ui.buttons.check(True, label="C2")
c3 = page.ui.buttons.check(False, label="C3", icon="fas fa-align-center")

# Based checkbox input component
c4 = page.ui.inputs.checkbox(False).tooltip("C4")

# Field component
c5 = page.ui.fields.checkbox(False, label="C5")

# checks list
data = [{"label": "python", "value": False}, {"label": "Java", "value": 5}]
checks = page.ui.lists.checks(data)

c2.click([
  # Write the full details of C2
  c.dom.write(c2.dom.val, stringify=True)
], [
  # Check another checkbox
  c3.js.checked()
])

page.ui.button("click").click([
  # Change the label
  c2.label.build("Ok"),
  c3.js.unchecked(),

  # Write the content of the checkbox in C5
  c.dom.write(c5.input.dom.content),

  # Write the content and details of C4
  c.dom.write(c4.dom.content),
  c.dom.write(c4.dom.val, stringify=True)
])

page.ui.button("Check c3").click([
  c3.js.checked()
])



