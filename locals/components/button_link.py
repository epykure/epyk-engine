
from epyk.core.Page import Report


# Defaults_css.Font.size = 20
# Create a basic report object
page = Report()
page.headers.dev()

page.ui.components_skin = {
  "button": {"css": {"color": "red"}, 'cls': ["cssbuttonbasic"]},
}

# Create a link to a page in a new tab
button = page.ui.button("Go go Google")
button.goto("www.google.fr")


# Create a link to a page within the same tab
button2 = page.ui.button("Go go Google")
button2.goto("www.google.fr", target="_self")
