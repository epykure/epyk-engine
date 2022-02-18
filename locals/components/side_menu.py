
from epyk.core.Page import Report


page = Report()
page.headers.dev()

#
menu = page.ui.contextual(["Super", 'next'])
menu.add_item('test', 'fas fa-times')
menu[0].click([
  page.js.alert("Test")
])

page.ui.layouts.new_line(10)
t = page.ui.text("Test")
t.contextMenu(menu, [])

menu2 = page.ui.contextual([])
for d in [{'label': 'Python', 'url': 'https://www.python.org/'}, {'label': 'R'}]:
  menu2 += page.ui.link(d['label'], d.get('url'))

page.ui.layouts.new_line(5)
t2 = page.ui.text("Test")
t2.contextMenu(menu2, [])

i = page.ui.fields.input("test", label="test", options={"select": True})
i2 = page.ui.fields.integer(options={"quantity": True, "select": True})
page.ui.fields.static(label="readonly field")

b = page.ui.button("Click")
page.ui.navigation.side([i, i2, b], position="left")
# size = 200
# d = page.ui.div("XXXXXXXXXXXXXXX")
# d.css({"position": 'absolute', 'top': 0, 'right': 0, 'height': '100%', 'overflow-x': 'hidden', 'margin-right': "-%spx" % size,
#        'width': "%spx" % size, 'border-left': '1px solid %s' % page.theme.colors[5], 'padding': '5px'})
# page.body.style.css.overflow_x = 'hidden'
#
# page.ui.button("Click").click([
#   d.dom.toggle_transition("margin-right", "0px", "-%spx" % size),
# ])

