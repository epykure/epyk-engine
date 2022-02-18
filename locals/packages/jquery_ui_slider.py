
import epyk as pk


page = pk.Page()
page.headers.dev()

# Console component
c = page.ui.rich.console(
  "* This is a log section for all the events in the different buttons *", options={"timestamp": True})


s1 = page.ui.slider(40)
s1.options.max = 300

s2 = page.ui.slider(40)
s2.options.disabled = True

#
row = page.ui.row([
  s1, s2
])

# Create a simple slider
s3 = page.ui.slider(40)
s3.change([
  c.dom.write(s3.dom.content),
]).css({"margin-bottom": "5px"})

# Add a slider based on a range of numbers
s4 = page.ui.sliders.range([12, 546, 98])

page.ui.layouts.hr()

# Set a slider of dates
s5 = page.ui.sliders.date("2020-01-02", minimum="2020-01-01", maximum="2020-12-31")
s5.options.range = "min"

page.ui.layouts.hr()

# Set a slider for a range of dates
s6 = page.ui.sliders.date_range("2020-01-02", "2020-06-02", minimum="2020-01-01", maximum="2020-12-31")

for col in row:
  col.css({"padding": '5px'})

# Add event on the progress bar to change and retrieve the value
page.ui.button("click").click([
  c.dom.write(s1.dom.content),
  c.dom.write(s4.dom.content),
  c.dom.write(s5.dom.content),
  c.dom.write(s2.dom.val, stringify=True),
])

page.ui.button("Enable").click([
  s2.js.enable(),
  c.dom.write(s6.dom.content),
])

page.ui.button("Set 150").click([
  s1.build(150)
])

c.move()

