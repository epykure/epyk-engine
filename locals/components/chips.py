
import epyk as pk


page = pk.Page()
page.headers.dev()

# Console component
c = page.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

#
ch = page.ui.chips(["example", {"value": 'test', 'name': 'group 2'}], options={"visible": True})
ch.append("new data")
ch.enter([

])

# Print Ok if shit+L is pressed in the input area of the chips component.
ch.keyup.shift_with('L', [
  page.js.alert("Ok")
])

bt1 = page.ui.button('Click').click([
  ch.dom.add(ch.dom.input),
  c.dom.write(ch.dom.content)
])

#
bt2 = page.ui.button('Add Fixed').click([
  ch.dom.add(ch.dom.input, category="other", fixed=True),
  c.dom.write(ch.dom.content, stringify=True),
  c.dom.write(ch.dom.values('group')),
  c.dom.write(ch.dom.values()),
])

#
icons = page.ui.icons.bar(['fas fa-times', 'fas fa-anchor'])
icons[0].click([
  page.js.alert("test")
])



