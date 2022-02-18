
import epyk as pk


page = pk.Page()
page.headers.dev()

# Console component
console = page.ui.rich.console(
  "This is a log section for all the events in the different buttons *", options={"timestamp": True})

css1 = page.ui.codes.css('''
''')

# py1 = page.ui.codes.python('''
# def test(a):
#   return a
# ''')

console.move()

page.ui.button("Click").click([
  #css1.js.refresh(),
  css1.js.setOption("mode", 'css'),
  css1.js.refresh(),
])

