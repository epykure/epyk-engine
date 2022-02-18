
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

record = [
  {"text": 'Text 1', "value": "text 1"},
  {"text": 'Text 2', "value": "text 2"},
  {"text": 'Text 3', "value": "text 3"},
]

select = page.ui.select(record)
select.options.selected = "text 2"
