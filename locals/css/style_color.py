
from epyk.core.Page import Report
from epyk.core.css import Colors
from epyk.core.css.themes import ThemeBlue


# Create a basic report object
page = Report()
page.headers.dev()
page.theme = ThemeBlue.BlueGrey()
page.body.add_template(defined_style="doc")

# Add HTML title
page.ui.title("Colors", 2)
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

# Get data from another defined theme
from epyk.core.css.themes import ThemeBlue

page.ui.title("Blue Theme", 4)

other_theme = ThemeBlue.Blue()
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
