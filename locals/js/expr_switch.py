
from epyk.core.Page import Report

from epyk.core.js import expr
from epyk.core.css.themes import ThemeBlue


# Create a basic report object
page = Report()
page.headers.dev()
page.theme = ThemeBlue.BlueGrey()
page.body.add_template(defined_style="doc")


page.ui.title("JavaScript Switch statement")

h = page.ui.texts.highlights(
  "This illustrates how to add switch statement from Pythons. The below shows how to change CSS Style attributes from "
  "a component value",
  icon="fab fa-js", type="info", options={"close": False})
h.style.css.background = "#f0db4f"

slider = page.ui.slider()

page.ui.titles.subtitle("Selected Number")
result = page.ui.div("No value selected")

slider.change([
  expr.switch(slider)
    .caseAbove(25, [result.dom.css({"color": "green"}).r])
    .caseRange(10, 24, [result.dom.css({"color": "black"}).r])
    .caseBelow(10, [
      result.dom.css({"color": "red"}).r
  ], include_value=False),
  result.build(slider.dom.content)
])

page.ui.layouts.hr()
page.ui.titles.subtitle("Report powered by")
page.ui.rich.powered()


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()
