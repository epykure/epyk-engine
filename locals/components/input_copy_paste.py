
from epyk.core.Page import Report

# Using data and JavaScript shortcuts
from epyk.core.js import std
from epyk.core.data import events


# Create a basic report object
page = Report()
page.headers.dev()

d = page.ui.div("Test")
d2 = page.ui.div()
d.paste([
  std.alert(events.event.clipboardData.text),
  d2.build(events.data)])

