
import epyk as pk

# Create a basic report object
page = pk.Page()
page.headers.dev()


button = page.ui.button("Test")

d = page.ui.drawers.right()
d.add_panel(page.ui.button("Test1"), "ok1")
d.add_panel(page.ui.button("Test2"), "ok2")
d.add_panel(page.ui.button("Test3"), "ok3")
d.set_handle(button)


d.drawers[0].click([
  d.dom.hide(),
  d.panels[0].dom.css({"display": 'block'}).r,
  page.js.console.log(d.dom.content)
])

d.drawers[1].click([
  d.dom.hide(),
  d.panels[1].dom.css({"display": 'block'}),
  d.dom.delete(1)
])

d.drawers[2].click([
  d.dom.hide(),
  d.panels[2].dom.css({"display": 'block'}).r])

d1 = page.ui.drawer(
  helper="This is a drawer example")
d1.add_panel(page.ui.button("Test"), "ok")
d1.drawers[0].click([d1.panels[0].dom.css({"display": 'block'})])

d2 = page.ui.drawers.no_handle(
  page.ui.button("No Handle"),
  helper="This is a drawer example"
)

page.ui.row([d, d1])

