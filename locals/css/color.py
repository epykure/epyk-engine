
import config

from epyk.core.Page import Report
from epyk.core.css import Colors

# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

# Add HTML title
rptObj.ui.title("Colors", 2)
rptObj.ui.title("Color component", 3)

# Add a HTML color component
rptObj.ui.images.color("red")

# Convert the colors to RGB
rgb = Colors.getHexToRgb("#FF0000")
rgba = Colors.rgba(*rgb, alpha=.5)

# Display a color
rptObj.ui.images.color(rgba, color="black")

# Display a range of colors
rptObj.ui.title("Panel colors", 3)
table = rptObj.ui.layouts.table(options={"header": False})
table.style.css.margin_top = 5

# Load the data to the table
range_colors = [rptObj.ui.images.color(c, color="black") for c in Colors.colors("#ffffff", "#FF0000", 30)]
table.from_array(range_colors, 4)

# Add an HTML title
rptObj.ui.title("Theme", 3)
rptObj.ui.title("Current", 4)

# Display the current theme colors
table = rptObj.ui.layouts.table(options={"header": False})
table.line("base colors", dim=4)
table.from_array([rptObj.ui.images.color(c, color="black") for c in rptObj.theme.colors], 4)
table.line("grey colors")
table.from_array([rptObj.ui.images.color(c, color="black") for c in rptObj.theme.greys], 4)
table.line("charts colors")
table.from_array([rptObj.ui.images.color(c, color="black") for c in rptObj.theme.charts], 4)

# Get data from another defined theme
from epyk.core.css.themes import ThemeBlue

rptObj.ui.title("Blue Theme", 4)

other_theme = ThemeBlue.Blue()
table = rptObj.ui.layouts.table(options={"header": False})
table.line("base colors", dim=4)
table.from_array([rptObj.ui.images.color(c, color="black") for c in other_theme.colors], 4)
table.line("grey colors")
table.from_array([rptObj.ui.images.color(c, color="black") for c in other_theme.greys], 4)
table.line("charts colors")
table.from_array([rptObj.ui.images.color(c, color="black") for c in other_theme.charts], 4)

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
