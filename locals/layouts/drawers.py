# https://developers.google.com/maps/documentation

import epyk as pk


# Create a basic report object
page = pk.Page()
page.headers.dev()

menu1 = page.ui.div("menu 1", html_code="test_menu_1")
menu2 = page.ui.div("menu2", html_code="test_menu_2")

menus = page.ui.div([menu1, menu2])
menus.style.css.height = 0
menus.style.css.padding_bottom = 10
menus.style.css.border_bottom = '1px solid %s' % page.theme.notch()

for c in menus.components.values():
  c.style.css.display = False

divA = page.ui.text("Test 1")
divA.style.add_classes.div.color_background_hover()
divB = page.ui.text("Test 2")
divB.style.add_classes.div.color_background_hover()

menu_mapping = {divA: menu1, divB: menu2}

div = page.ui.div([divA, divB], options={'inline': True})
for c in div.components.values():
  c.style.css.padding = "0 5px"

menus.move()
div.style.css.background = page.theme.notch()
div.style.css.color = 'white'
div.style.css.padding = '5px 0'


for menu_item, panel in menu_mapping.items():
  menu_item.click([
    pk.js_std.querySelectorAll(
      pk.js_std.selector(menus).with_child_element("div").excluding(panel)).css({"display": 'none'}),
    #
    pk.js_expr.if_(pk.js_std.querySelector(pk.js_std.selector(menus)).getAttribute("data-panel") == menu_item.htmlCode, [
      pk.js_std.querySelector(pk.js_std.selector(menus)).setAttribute("data-panel", ""),
      pk.js_std.querySelector(pk.js_std.selector(menus)).css({"height": 0, "top": 0})
    ]).else_([
      pk.js_std.querySelector(pk.js_std.selector(menus)).setAttribute("data-panel", menu_item.htmlCode),
      pk.js_std.querySelector(pk.js_std.selector(menus)).css({"height": "auto", "top": "30px"})
    ]),
    pk.js_std.querySelector(pk.js_std.selector(panel)).css({'display': 'block'})
  ])

