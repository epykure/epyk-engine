# http://jsfiddle.net/KUCaL/

import epyk as pk

from epyk.core.css import Defaults


#
#Defaults.BACKGROUND = None
Defaults.BODY_CONTAINER = {"border": None}

# Create a basic report object
page = pk.Page()
page.headers.dev()

page.theme = pk.themes.ThemeDark.Dark()

# Console component
c = page.ui.rich.console(
  "* This is a log section for all the events in the different buttons *", options={"timestamp": True})

page.ui.layouts.iframe("http://www.google.com")

#
dd = page.ui.icon("fas fa-arrow-down").css(
  {"border": '1px solid black', "position": 'fixed', "width": 'none',
   "border-radius": '20px', "padding": '8px', "left": '20px'})

du = page.ui.icon("fas fa-arrow-up").css(
  {"border": '1px solid black', "position": 'fixed', "width": 'none',
   "border-radius": '20px', "padding": '8px', "left": '20px', "bottom": "20px"})

#page.ui.navigation.down()
page.ui.navigation.pin("test")

du = page.ui.navigation.to(100, tooltip="test")
#
ind = page.ui.navigation.indices(10)
#
# p = page.ui.navigation.points(10)
# d = page.ui.navigation.dots(10)
#
# p.options.background_color = "orange"
# b = page.ui.button("test")
#
# for i, _ in enumerate(p):
#   p.click(i, [b.build(page.js.objects.this), page.js.console.log(page.js.objects.this.getAttribute("data-position"))])
#   d.click(i, [])
#   ind.click(i, [])

# tab = page.ui.layouts.pills()
# tab.add_panel("test", page.ui.div("Test Content"))
# tab.add_panel("test 2", page.ui.div("Test Content 2"))


# tab2 = page.ui.layouts.tabs()
# tab2.add_panel("test", page.ui.div("Test Content"))
# tab2.add_panel("test 2", page.ui.layouts.col([
#   page.ui.div("Test Content 3")]))


#div = page.ui.layouts.panelsplit(left=number, right=number_2, resizable=True)
#div = page.ui.layouts.tabs([number, number_3, number_2, number_4])

page.ui.layouts.dialogs()

page.ui.layouts.hr()

page.ui.layouts.new_line(5)

for i in range(70, 100):
  t = page.ui.text(
    "this [test](http://www.google.com) !(fab fa-python) --is-- ***an*** *example*, **ok**", options={"limit_char": i})
  t.options.markdown = True
  #page.js.addOnLoad(t.refresh())

page.ui.layouts.new_line(50)

# d.drop([
#   page.js.objects.data.toRecord([1, 2, 3, 4], "result"),
#   c.write(page.js.objects.event.dataTransfer.text)
# ])

#
# du.click([
#   c.write("ok")
# ])

t = page.ui.text("Test")
t.click([
  page.js.objects.event.stopPropagation(),
  page.js.objects.event.preventDefault(),
  c.dom.write("Message from the text box"),
  c.dom.write(t.dom.content),
])

print(page.css.button.basic())

#d + t

#page.js.addOnLoad(
#  page.js.window.events.addContentLoaded(page.js.alert("DOM fully loaded and parsed"))
  #page.js.window.addEventListener("scroll", page.js.alert(page.js.window.scrollY))
#)

c.move()

page.headers.title("title")
page.headers.favicon('https://github.com/favicon.ico')
page.headers.meta.custom('language', 'python')

