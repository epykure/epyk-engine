import epyk as pk

NAME = "Effects & Transitions"

# Create a basic report object
page = pk.Page()

page.ui.titles.title(NAME)
h = page.ui.texts.highlights('''
This illustrates how to animate components with effects and transitions.
Main concepts will be how to:
- Animate your page using transitions from the dom property
- Add predefined effects from the property ``.style.effects``
''', icon="fab fa-css3-alt", type="info", color="white", options={"close": False, "markdown": True})
h.style.css.background = "#4C6EF5"
page.ui.layouts.hr()

# Dom events are available on each components and they will be more detailed on the Javascript section
# CSS effects are mainly driven by Javascript function
div = page.ui.div("This is a text")
div.style.css.cursor = 'pointer'

div.click([
  # Change the color to red for 1 second
  div.dom.transition("color", "red", duration=1, reverse=True)
])

# CSS animate can also be done using transition effects
# There is a catalog of predefined effects
div = page.ui.div("This is a new text")
div.style.effects.blink(2)

# it possible to define a custom animation
div = page.ui.div("This is a animated text")
div.style.effects.animate('test - animate', {"color": "red", "padding-left": "200px"}, delay=5, iteration_count=False)

# Adding classes to the framework
from epyk.core.css.styles.classes import CssStyle


class CssHoverColor(CssStyle.Style):
  _attrs = {'color': 'blue', 'cursor': 'pointer'}
  _hover = {'color': 'orange'}


# Bespoke component creation
div_a = page.ui.div("Div with shared class")
div_b = page.ui.div("Div with shared class")

div_a.style.add_classes.custom(CssHoverColor)
div_b.style.add_classes.custom(CssHoverColor)

# Overriding advances CSS attributes (hover, focus, after, before)
# This will create a CSS class for the component and it will add all the inline CSS definition to it automatically
# The style attribute of the component will then be empty
div = page.ui.div("This is a text with an interactive style")
div.style.css.padding = 10
div.style.hover({"color": 'green'})

INFOS = '''
Animation and effects
'''


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()

