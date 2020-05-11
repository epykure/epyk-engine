
import config

from epyk.core.Page import Report

# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

record = [
  {"text": 'text', 'icon': 'fas fa-times', 'checked': True, 'value': 8},
  {"text": 'abc', 'icon': 'fas fa-times', 'checked': True, 'value': 5},
  {"text": 'def', 'icon': 'fas fa-times', 'checked': True, 'value': 5},
  {"text": 'ghi', 'icon': 'fas fa-times', 'checked': True, 'value': 5},
]

data = rptObj.data.js(records=record)
search = rptObj.ui.inputs.search()

list = rptObj.ui.lists.items(record, options={"badge": {"background": 'green'}, 'delete': True})

filter = data.filterGroup("test_filter")
search.enter([
  rptObj.js.console.log(list.dom.content),
  list.build(filter.any(search.dom.content))
])


rptObj.ui.button("Button").click([
  list.dom.getItemByValue(search.dom.content).css({"color": 'red'})
])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)