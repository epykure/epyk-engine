
import epyk as pk


page = pk.Page()
page.headers.dev()

# Console component
c = page.ui.rich.console(
  "* This is a log section for all the events in the different buttons *", options={"timestamp": True})

#
field = page.ui.fields.autocomplete(label="Label")

#
text = page.ui.inputs.autocomplete()
text.options.source = ["abs"]

#
page.ui.button("click").click([
  c.dom.write(field.input.dom.content)
])

#
page.ui.button("Empty").click([
  field.input.dom.empty(),
  text.dom.empty(),
])

c.move()

