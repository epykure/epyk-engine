
from epyk.core.Page import Report

# change the Framework default styles
from epyk.core.css import Defaults


# Create a basic report object
page = Report()
page.headers.dev()
page.body.add_template(defined_style="doc")

page.ui.titles.title("CSS Inline styles")
page.ui.texts.highlights(
  "Change the style of components using inline CSS property from *style.css.*",
  icon="fas fa-search-plus", type="info", options={"close": False, 'markdown': True})
# Create component
div = page.ui.div("This is a container 1")

# Get the default CSS styles
page.ui.print(div.style.css)

# Change the CSS Style
# all the CSS properties are available and are documented
div.style.css.color = "red"
div.style.css.display = "inline-block"
div.style.css.width = "auto"

# Those inline CSS properties will override the ones defined in the CSS classes
# The below method will return the CSS classes defined in this component
# The main will be added to it whereas the other will only be added to the page
page.ui.print(div.style.get_classes())


page.ui.texts.highlights(
  "Or use the css() function to replicate the Jquery shortcut",
  icon="fas fa-search-plus", type="info", options={"close": False})
# using a Jquery like function
div.css({"border": '1px solid black'})

# Remove the CSS style for the defined component
cont = page.ui.div("This is a container 2")
cont.style.clear_style()
page.ui.print(div.style.css)

# Since this point the default values will be changed and the components will use then to get their styles
# Defaults.Font.size = 20

div2 = page.ui.div("This is a container 3")

# Some functions are available to avoid changing the common reference
div3 = page.ui.div("This is a container 4")
# -5 from the reference
div3.style.css.font_size = Defaults.font(-5)

INFOS = '''

'''

if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()
