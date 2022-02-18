
import epyk as pk

NAME = "inline properties"

# Create a basic report object
page = pk.Page()

page.ui.titles.title(NAME)
h = page.ui.texts.highlights('''
This illustrates how to change component styles using CSS inline properties.
Main concepts will be how to change the style of components using:
- Inline CSS property from ``style.css.``
- Or the css() function to replicate the Jquery shortcut
''', icon="fab fa-css3-alt", type="info", color="white", options={"close": False, "markdown": True})
h.style.css.background = "#4C6EF5"
page.ui.layouts.hr()

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
div3.style.css.font_factor(-5)

INFOS = '''

'''

if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()
