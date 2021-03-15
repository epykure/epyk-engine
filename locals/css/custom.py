
from epyk.core.Page import Report
from epyk.core.css.themes import ThemeBlue


# Create a basic report object
page = Report()
page.headers.dev()
page.theme = ThemeBlue.BlueGrey()
page.body.add_template(defined_style="doc")

title = page.ui.titles.title("Custom CSS Classes")
page.ui.texts.highlights(
  "Load external CSS modules from the page: animate.min.css",
  icon="fas fa-search-plus", type="info", options={"close": False})

# https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.2/animate.min.css
page.css.customFile("animate.min.css", path="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.2")

# Add the file from the local environment context defined in Imports.STATIC_PATH
# This path will be overridden and specific to your configuration
page.css.customFile("test.css")

page.ui.texts.highlights(
  "Add a CSS Class directly from a Python String",
  icon="fas fa-search-plus", type="info", options={"close": False})

# Create CSS text fragments to be added to the final HTML page
page.css.customText('''
.red_color {
  color: red
 }
''')

page.ui.texts.highlights(
  "Attached to the style to HTML components",
  icon="fas fa-search-plus", type="info", options={"close": False})

page.ui.titles.subtitle("Result")
# Bespoke component creation
t = page.ui.text("test")

# Attach the bespoke CSS class deduced from the text fragment
t.style.add_classes.external("red_color")

# Basic library use
# more details here: https://github.com/daneden/animate.css#Basic-Usage
t2 = page.ui.text("test")

# Attach a CSS class from the animate.min.css module
t2.style.add_classes.external(["animated", "bounce"])

# Create a bespoke CSS class from the Python framework
# => target being to get this included at some point in the official package
from epyk.core.css.styles.classes import CssStyle


class CssHoverColor(CssStyle.Style):
  _attrs = {'color': 'blue', 'cursor': 'pointer'}
  _hover = {'color': 'orange'}


# Bespoke component creation
div = page.ui.div("This is a container")

# Attach the class to the component
div.style.add_classes.custom(CssHoverColor)


class CssBodyMargin(CssStyle.Style):
  _attrs = {'padding': '0 40px'}


# same thing can be added to the body
page.body.style.add_classes.custom(CssBodyMargin)

# it is important to keep in mind that the inline CSS style of any component will be used in priority compared
# to the styles in a CSS class
v_cls = page.css.anonymous_cls({
  '_attrs': {'color': 'green', 'cursor': 'pointer'},
  '_hover': {'color': 'red'}})

# Bespoke component creation
div2 = page.ui.div("This is a container")
div2.style.add_classes.custom(v_cls)


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()
