
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

record = [
  {"text": 'text', 'icon': 'fas fa-times', 'checked': True, 'value': 8},
  {"text": 'abc', 'icon': 'fas fa-times', 'checked': True, 'value': 5},
  {"text": 'def', 'icon': 'fas fa-times', 'checked': True, 'value': 5},
  {"text": 'ghi', 'icon': 'fas fa-times', 'checked': True, 'value': 5},
]

data = page.data.js.record(data=record)

# Add a search input text
search = page.ui.inputs.search()

list = page.ui.lists.items(record, options={"badge": {"background": 'green'}, 'delete': True})

# Create a filter dimension
filter = data.filterGroup("test_filter")

# Add an event on the search component
search.enter([
  # filter based on the content of the search input text
  list.build(filter.any(search.dom.content))
])

