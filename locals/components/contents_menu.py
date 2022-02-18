
from epyk.core.Page import Report


page = Report()
page.headers.dev()

menu = page.ui.contents()
menu.add(page.ui.text("Simple text"))
menu.anchor("Test", 3, "#name")
page.ui.button("Button").click([
  menu.build([{"text": 'ok', "level": 0, "anchor": "#test"}])
])

page.ui.layouts.br(150)
page.ui.div("Title Test", html_code="name")
page.ui.layouts.br(50)
page.ui.div("Title Test", html_code="test")
page.ui.layouts.br(150)