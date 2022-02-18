
import epyk as pk


# Create a basic report object
page = pk.Page()
page.headers.dev()

t0 = page.ui.titles.section("Available Items")
items = page.ui.list(["A", "B", "C"])
for i in items:
  i.draggable()

t1 = page.ui.titles.section("Drop an item below")
div = page.ui.div("No dropped value", html_code='drop_zone')
div.style.css.padding = 5
div.style.css.background = page.theme.colors[0]
div.style.css.border = "1px dashed %s" % page.theme.colors[-1]
div.drop([
  div.build(pk.events.data)
])

item_name = page.ui.input()
bt = page.ui.button("add").click([
  items.dom.add(item_name.dom.content)
])

