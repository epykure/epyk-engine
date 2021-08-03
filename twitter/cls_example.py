
import epyk as pk


# Create CSS classes
css = pk.CssInline()
css.color = "red"
css.important(["color"])

page = pk.Page()
css.define_class("textColor", page)

t = page.ui.text("Color will change when mouse hover")
t.style.css.cursor = "pointer"
t.style.css.color = "green"

t.mouse([
  t.dom.toggleClass("textColor").r
], [
  t.dom.toggleClass("textColor").r
])

# Write the static HTML result
page.outs.html_file(name="outCssClsExample")
