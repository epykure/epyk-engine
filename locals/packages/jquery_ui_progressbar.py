
import epyk as pk


page = pk.Page()
page.headers.dev()

# Console component
c = page.ui.rich.console(
  "* This is a log section for all the events in the different buttons *", options={"timestamp": True})

# Create a progressbar (max 100)
b1 = page.ui.sliders.progressbar(300, total=300)
b1.options.background = "red"

b2 = page.ui.sliders.progressbar(50)

# Add event on the progress bar to change and retrieve the value
page.ui.button("click").click([
  c.dom.write(b2.dom.content),
  b1.build(20),
  c.dom.write(b1.dom.val, stringify=True),
])

c.move()

