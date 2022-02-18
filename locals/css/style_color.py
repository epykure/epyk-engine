
import epyk as pk
from epyk.core.css import Colors

NAME = "Colors"

# Create a basic report object
page = pk.Page()

page.ui.title(NAME)
h = page.ui.texts.highlights('''
Display the colors definition for the default theme.
''', icon="fab fa-css3-alt", type="info", color="white", options={"close": False})
h.style.css.background = "#4C6EF5"
page.ui.layouts.hr()

# Add HTML title
page.ui.title("Color component", 3)

# Add a HTML color component
page.ui.images.color("red")

# Convert the colors to RGB
rgb = Colors.getHexToRgb("#FF0000")
rgba = Colors.rgba(*rgb, alpha=.5)

# Display a color
page.ui.images.color(rgba, color="black")

# Display a range of colors
page.ui.title("Panel colors", 3)
table = page.ui.layouts.table(options={"header": False})
table.style.css.margin_top = 5

# Load the data to the table
range_colors = [page.ui.images.color(c, color="black") for c in Colors.colors("#ffffff", "#FF0000", 30)]
table.from_array(range_colors, 4)

# Add an HTML title
page.ui.title("Theme", 3)
page.ui.title("Current", 4)

# Display the current theme colors
table = page.ui.layouts.table(options={"header": False})
table.line("base colors", dim=4)
table.from_array([page.ui.images.color(c, color="black") for c in page.theme.colors], 4)
table.line("grey colors")
table.from_array([page.ui.images.color(c, color="black") for c in page.theme.greys], 4)
table.line("charts colors")
table.from_array([page.ui.images.color(c, color="black") for c in page.theme.charts], 4)

page.ui.title("Blue Theme", 4)

other_theme = pk.themes.ThemeBlue.Blue()
table = page.ui.layouts.table(options={"header": False})
table.line("base colors", dim=4)
table.from_array([page.ui.images.color(c, color="black") for c in other_theme.colors], 4)
table.line("grey colors")
table.from_array([page.ui.images.color(c, color="black") for c in other_theme.greys], 4)
table.line("charts colors")
table.from_array([page.ui.images.color(c, color="black") for c in other_theme.charts], 4)


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()
