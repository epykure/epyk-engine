
import epyk as pk


page = pk.Page()
page.headers.dev()

# Console component
c = page.ui.rich.console(
  "* This is a log section for all the events in the different buttons *", options={"timestamp": True})

current = page.ui.menus.selections([])

#
modal = page.ui.modals.dialog("rsr")
modal.options.title = "Test Modal"

#
input = page.ui.input("")
input_hide = page.ui.inputs.hidden("Hidden text")

#
page.ui.button("click").click([
  modal.build(input_hide.dom.content),
  modal.js.open()
])

c.move()

