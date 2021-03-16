
from epyk.core.Page import Report
from epyk.core.js import std
from epyk.core.css.themes import ThemeBlue


# Create a basic report object
page = Report()
page.headers.dev()
page.theme = ThemeBlue.BlueGrey()
page.body.add_template(defined_style="doc")

page.ui.components_skin = {"button": {"css": {"background": "#323330", "color": "#f0db4f", "border-color": "#323330"}}}

page.ui.title("JavaScript - QuerySelectors")

h = page.ui.texts.highlights(
  "This illustrates how to use QuerySelectors to change DOM components on the page",
  icon="fab fa-js", type="info", options={"close": False})
h.style.css.background = "#f0db4f"

button1 = page.ui.button("Button 1")
button2 = page.ui.button("Button 1")
button3 = page.ui.button("Button 1")


div1 = page.ui.div("div 1")
div2 = page.ui.div("div 2")
div3 = page.ui.div("div 3")

div = page.ui.div([div1, div2, div3])


button1.click([
  std.querySelectorAll(std.selector(div).with_child_element("div").excluding(div1)).css({"display": 'none'}),
  std.querySelector(std.selector(div1)).css({"display": 'block'})
])

button2.click([
  std.querySelectorAll(std.selector(div).with_child_element("div").excluding(div2)).css({"display": 'none'}),
  std.querySelector(std.selector(div2)).css({"display": 'block'})
])

button3.click([
  std.querySelectorAll(std.selector(div).with_child_element("div").excluding(div3)).css({"display": 'none'}),
  std.querySelector(std.selector(div3)).css({"display": 'block'})
])

page.ui.layouts.hr()
page.ui.titles.subtitle("Report powered by")
page.ui.rich.powered()


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()
