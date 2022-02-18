
import epyk as pk

NAME = "Classes"


# Create a basic report object
page = pk.Page()

page.ui.titles.title(NAME)
h = page.ui.texts.highlights('''
This illustrates how to change component styles using CSS Classes.
The page will show how to:
- Display the default CSS classes for a common container (a HTML tag) with ``style.classList``
- A a specific predefined class using ``.style.add_classes.text.colored()``
- Create of a bespoke CSS class from Python.
''', icon="fab fa-css3-alt", type="info", color="white", options={"close": False, "markdown": True})
h.style.css.background = "#4C6EF5"

page.ui.layouts.hr()

div = page.ui.div("This is a text in a div container")
# Classlist like feature to access all the classes loaded for a given object
# Classes are not supposed to be changed and they are properties shared across components
for label, sections in div.style.classList.items():
  page.ui.titles.subtitle("CSS Class Category: %s" % label)
  for v in sections:
    page.ui.print(v)

# All the classes in the framework are located in the catalog in the style property using add_classes
div.style.add_classes.text.colored()
for label, sections in div.style.classList.items():
  page.ui.titles.subtitle("CSS Class Category: %s" % label)
  for v in sections:
    page.ui.print(v).css({"white-space": "None"})


# Create a bespoke CSS class from the Python framework
# => target being to get this included at some point in the official package
from epyk.core.css.styles.classes import CssStyle


class CssHoverColor(CssStyle.Style):
  _attrs = {'color': 'blue', 'cursor': 'pointer'}
  _hover = {'color': 'orange'}

div1 = page.ui.div("This is a text")
# Attach the class to the component
div1.style.add_classes.custom(CssHoverColor)

# Example of use of data content to fill a CSS attribute
div = page.ui.div("")
div.style.attr_content("data-content")
div.attr["data-content"] = 'Blue Content'


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()


