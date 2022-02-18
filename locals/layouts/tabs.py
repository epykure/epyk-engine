
import epyk as pk


# Create a basic report object
page = pk.Page()
page.headers.dev()

#
tabs = page.ui.panels.tabs()
tabs.options.css_tab_clicked = {"border-bottom": '1px solid red', "background": 'white'}

for i in range(5):
  if i % 2:
    tabs.add_panel("Panel %s" % i, page.ui.text("test %s" % i), css_tab_clicked={"background": 'yellow'})
  else:
    tabs.add_panel("Panel %s" % i, page.ui.text("test %s" % i), selected=True)
tabs.select("Panel 2")

page.ui.button("Click").click([
  tabs.dom.add_tab("New tab"),
  page.js.console.log(tabs.dom.selected_index),
  tabs.dom.deselect_tabs(),
  tabs.panel("Panel 2").dom.transition("color", 'red', duration=1, reverse=True)
])

up = page.ui.panels.arrows_up()
for i in range(5):
  up.add_panel("Panel %s" % i, page.ui.text("test %s" % i), selected=True)

down = page.ui.panels.arrows_down()
for i in range(5):
  down.add_panel("Panel %s" % i, page.ui.text("test %s" % i), selected=True)

menu = page.ui.panels.menu()
for i in range(5):
  menu.add_panel("Panel %s" % i, page.ui.text("test %s" % i), selected=True)

pills = page.ui.panels.pills()
for i in range(5):
  pills.add_panel("Panel %s" % i, page.ui.text("test %s" % i), selected=True)
