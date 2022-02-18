
import epyk as pk
from epyk.core.data import http


page = pk.Page()
page.headers.dev()

shortcuts = page.ui.navigation.shortcut([
  'fab fa-python',
  'fab fa-rust',
  'fab fa-js'
])


# Change the URL on the side bar wiht URL values
# epyk-templates/outs/html/locals_layouts_shortcut.html?icon=python
shortcuts[0].tooltip("This is Python")
shortcuts[0].goto(http.get("icon").toString().prepend("https://fontawesome.com/icons/"))