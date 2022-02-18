
import epyk as pk


# Create a basic report object
page = pk.Page()
page.headers.dev()

page.ui.layouts.new_line(20)
page.ui.button("Click").click([
  page.js.alert(page.js.window.scrollPercentage)
])

page.ui.layouts.new_line(20)

page.ui.button("Click 2").click([
  page.js.alert(page.js.window.scrollPercentage)
])

page.ui.layouts.new_line(20)

page.ui.button("Click 3").click([
  page.js.alert(page.js.window.scrollPercentage)
])


page.ui.layouts.new_line(20)

page.ui.button("Click 4").click([
  page.js.alert(page.js.window.scrollPercentage)
])

page.ui.layouts.new_line(20)

p = page.ui.navigation.scroll(60)

#page.ui.sliders.progressbar(0, height=(5, 'px'))

# page.js.addOnReady(
#   page.js.window.events.addScrollListener([
#     p.build(page.js.window.scrollPercentage)
# ]))

# p.style.css.fixed_top()
p.style.css.fixed_top()

page.ui.button("Click 5").click([
  p.build(page.js.window.scrollPercentage)
])

