
from epyk.core.Page import Report

# Defaults_css.Font.size = 20
# Create a basic report object
page = Report()
page.headers.dev()

page.ui.components_skin = {
  "buttons.absolute": {"clear": {"css": True, "cls": True}, "css": {"color": "red"}},
  "buttons.check": {"css": {"color": "red"}},
}

page.ui.buttons.absolute('Confirm')
page.ui.buttons.check(label='Confirm')