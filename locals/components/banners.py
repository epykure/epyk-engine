
from epyk.core.Page import Report
from epyk.core.css.themes import ThemeBlue


# Create a basic report object
page = Report()
page.headers.dev()
page.theme = ThemeBlue.BlueGrey()
page.body.add_template(defined_style="doc")

# Add a banner on top of the page
top = page.ui.banners.top("text")
top.style.css.font_size = '40px'

# Change the banner style
top.style.css.height = 100
top.style.css.text_align = "center"
top.style.css.vertical_align = "middle"

# Add a banner with HTML content
icon = page.ui.icon("fab fa-python")
text = page.ui.text("This is a text")

# Chang the option to have the content in one line
bottom = page.ui.banners.bottom([icon, text], options={"inline": True})

# Add a banner on the bottom right corner
b = page.ui.banners.corner("bottom", 'red')
# Add click event on the banner
b.click([
  # hide the bonner on click
  b.dom.hide()
])

# Add a banner on the top right conner
corner = page.ui.banners.corner("top", 'red', position='top')
# Add interactivity on the banner style
corner.style.hover({"background": "white", 'color': 'red'})

# Add event when mouse is on the component
corner.hover([
  # display the banner
  b.dom.show()
])

# Button to change the value of a banner
button = page.ui.button("Change")
button.style.css.margin_top = 150
button.click([
  corner.build("New test")
])