
from epyk.core.Page import Report
from epyk.core.data import tree
from epyk.core.data import events


# Create a basic report object
page = Report()
page.headers.dev()

data = [
  {"value": 'value', 'items': [
      {"value": 'value 1'},
      {"value": 'value 2', 'items': [
        {"value": 'value 3'},
        {"value": 'value 4'},
      ]},
      {"value": 'value A', 'items': [
        {"value": 'value A1'},
        {"value": 'value A2'},
      ]},
  ]}
]

d = page.ui.lists.dropdown(data)

tree_files = tree.folders(r"C:\tests")
f = page.ui.lists.dropdown(tree_files)

d.click([
  page.js.console.log(events.value)
])

f.click([
  page.js.console.log(events.value)
])