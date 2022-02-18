
import epyk as pk


# Create a basic report object
page = pk.Page()
page.headers.dev()
page.theme = pk.themes.ThemeBlue.BlueGrey()

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
  pk.js_std.querySelectorAll(pk.js_std.selector(div).with_child_element("div").excluding(div1)).css({"display": 'none'}),
  pk.js_std.querySelector(pk.js_std.selector(div1)).css({"display": 'block'})
])

button2.click([
  pk.js_std.querySelectorAll(pk.js_std.selector(div).with_child_element("div").excluding(div2)).css({"display": 'none'}),
  pk.js_std.querySelector(pk.js_std.selector(div2)).css({"display": 'block'})
])

button3.click([
  pk.js_std.querySelectorAll(pk.js_std.selector(div).with_child_element("div").excluding(div3)).css({"display": 'none'}),
  pk.js_std.querySelector(pk.js_std.selector(div3)).css({"display": 'block'})
])


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()
