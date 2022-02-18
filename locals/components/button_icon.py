
from epyk.core.Page import Report


# Defaults_css.Font.size = 20
# Create a basic report object
page = Report()
page.headers.dev()

b1 = page.ui.buttons.phone("Call")
b2 = page.ui.buttons.remove("Remove")
b3 = page.ui.buttons.small("Small Button")
b4 = page.ui.buttons.large("Large Button")
b5 = page.ui.buttons.colored("Large Button")
b6 = page.ui.buttons.thumbs_up(tooltip="Like")
b7 = page.ui.buttons.live(3, page.js.console.log("Click"), options={"started": False})
b8 = page.ui.buttons.live(2, page.js.console.log("refresh data"), profile=True)