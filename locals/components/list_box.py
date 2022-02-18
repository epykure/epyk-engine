
import epyk as pk


# Create a basic report object
page = pk.Page()
page.headers.dev()

title = page.ui.titles.title("List of boxes example")
item_title = page.ui.fields.input(label="title")
item_text = page.ui.fields.input(label="content")
button = page.ui.buttons.colored("Add", align="center")
hr = page.ui.layouts.hr()

lt = page.ui.lists.box([
  {"text": 'test', 'color': 'green', 'title': 'This is a file', 'icons': [
    {"icon": 'fab fa-js', 'click': 'alert(value)', 'tooltip': 'test'},
    {"icon": 'fab fa-python', 'click': 'alert(value)'},
  ]},
  {"text": 'test', 'title': 'This is another file', 'icons': [
    {"icon": 'fab fa-js', 'click': 'alert(value)'},
    {"icon": 'fab fa-python', 'click': 'alert(value)'},
  ]}
], width=(200, 'px'))

button.click([
  lt.dom.add({"text": item_text.input.dom.content, 'title': item_title.input.dom.content, 'icons': [
    {"icon": 'fab fa-js', 'click': 'alert(value)', 'color': 'red'},
    {"icon": 'fab fa-python', 'click': 'alert(value)'}
  ]})
])