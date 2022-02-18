
from epyk.core.Page import Report
from epyk.core.data import components
from epyk.mocks import urls as data_urls

# TODO add Js events and also improve fwk to add click from labels

# Create a basic report object
page = Report()
page.headers.dev()

#
data = page.py.requests.csv(data_urls.AIRPORT_TRAFFIC)

#
page.body.style.css.padding = "0 20px"

# Console component
c = page.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

#
radio_data = components.radio.from_records(data, 'city')
page.ui.radio(radio_data)

# Add a group of radio buttons
c1 = page.ui.fields.radio(True, label="Check 1", group_name="group1")
c2 = page.ui.fields.radio(True, label="Check 2", group_name="group1")

# Add a checked radio button
c3 = page.ui.inputs.radio(True, label="Check")

# Add a tick HTML component
c4 = page.ui.icons.tick(False, "Check")

# Add a list with radions buttons
c5 = page.ui.lists.radios([
  {"value": True, 'text': 'Python'},
  {"value": False, 'text': 'Javascript'},
])

c1.click([
  c.dom.write(c1.dom.content),
  c.dom.write(c1.dom.selected),
  c.dom.write(c3.dom.val, stringify=True)
])


# Click even
page.ui.button("click").click([
  c.dom.write(c4.dom.val, stringify=True),
  c.dom.write(c5.dom.content),

  # Check the value C1
  c1.js.check()
])

page.ui.button("Uncheck C1").click([
  # uncheck the value C1
  c1.js.uncheck(),
  # Change the label of the tick component
  c4.span.build("New Label"),
  # Change the color CSS property of the internal label
  c4.span.dom.css({"color": 'red'})
])
