
from epyk_studio.core.Page import Report

page = Report()
page.headers.dev()

b = page.studio.buttons.more([
  {"text": "Add", "target": "_blank", "icon": "fab fa-500px", "url": "https://stackoverflow.com/questions/5884066/hashing-a-dictionary"},
  {"text": "Delete", "target": "_blank", "icon": "fab fa-500px", "url": "https://stackoverflow.com/questions/5884066/hashing-a-dictionary"},
])
b.menu.options.items_type = "link"


b = page.studio.buttons.more([
  {"text": "Item 1"},
  {"text": "Item 2"},
], profile=True)

b.click([
  page.js.console.log("test")
])

u = page.ui.button("Update")
u.click([
  b.menu.build([
  {"text": "Item 1"},
  {"text": "Item 2"},
  {"text": "Item 3"},
  ])
])
