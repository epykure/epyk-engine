
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

# Add a simple navigation bar with two panels
nav = page.ui.panels.nav(options={"position": 'bottom'})
nav.add_panel("Test", page.ui.div("Container"))
nav.add_panel("Test 2", page.ui.div("Container 2"))

# Create a div container
page.ui.div([nav]).css({'border': '1px solid black', 'height': '200px'})

# Add a navigation panel with two tabs
nav2 = page.ui.navigation.panel()
nav2.add_panel("Test", page.ui.div("Container"))
nav2.add_panel("Test 2", page.ui.div("Container 2"))

page.ui.div([nav2]).css({'border': '1px solid black', 'height': '200px'})

