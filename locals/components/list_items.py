
import epyk as pk

from epyk.core.data import list_items
from epyk.mocks import urls as data_urls


# Create a basic report object
page = pk.Page()
page.headers.dev()

#
data = page.py.requests.csv(data_urls.COVID_US)

inputs = page.ui.input()

items1 = page.ui.lists.items(["value 1", "value 2"])
items2 = page.ui.lists.items(list_items.text.from_records(data, "state"))

items3 = page.ui.lists.links(
  list_items.link.from_records(
    data, "state", text=lambda x: "www.google.com?value=%(state)s" % x))

items4 = page.ui.lists.pills([
  {"text": "value 1"},
  {"text": "value 2"},
])

items5 = page.ui.lists.box(
  list_items.box.from_records(
    data, "state", title=lambda x: "Title - %(state)s" % x))

items6 = page.ui.lists.radios([
  {"text": "value 1", "value": "Content"},
  {"text": "value 2", "value": "Content"},
])

items7 = page.ui.lists.checks([
  {"text": "value 1", "value": "Content"},
  {"text": "value 2", "value": "Content"},
])

items8 = page.ui.lists.icons([
  {"icon": "fas fa-chart-pie", "text": "value 1"},
  {"icon": "fas fa-chart-pie", "text": "value 1"},
])

row = page.ui.row([
  items1, items2, items3, items4, items5, items6, items7, items8
], position="top")
row.options.responsive = False

inputs.enter([
  items1.dom.add(inputs.dom.content)
])