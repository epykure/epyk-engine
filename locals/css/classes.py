
from epyk.core.Page import Report
from epyk.core.css.themes import ThemeBlue


# Create a basic report object
page = Report()
page.headers.dev()
page.theme = ThemeBlue.BlueGrey()
page.body.add_template(defined_style="doc")


title = page.ui.titles.title("CSS Classes")
page.ui.texts.highlights(
  "The below will show the default CSS classes for a common container (a HTML tag)",
  icon="fas fa-search-plus", type="info", options={"close": False})

div = page.ui.div("This is a text in a div container")
# Classlist like feature to access all the classes loaded for a given object
# Classes are not supposed to be changed and they are properties shared across components
for label, sections in div.style.classList.items():
  page.ui.titles.subtitle("CSS Class Category: %s" % label)
  for v in sections:
    page.ui.print(v)


page.ui.texts.highlights(
  "A specific class will be added using *.style.add_classes.text.colored()*",
  icon="fas fa-search-plus", type="info", options={"close": False})

# All the classes in the framework are located in the catalog in the style property using add_classes
div.style.add_classes.text.colored()
for label, sections in div.style.classList.items():
  page.ui.titles.subtitle("CSS Class Category: %s" % label)
  for v in sections:
    page.ui.print(v).css({"white-space": "None"})


# Create a bespoke CSS class from the Python framework
# => target being to get this included at some point in the official package
from epyk.core.css.styles.classes import CssStyle


page.ui.texts.highlights(
  "Creation of a bespoke CSS class from Python",
  icon="fas fa-search-plus", type="info", options={"close": False})


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


