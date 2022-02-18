
import epyk as pk
from epyk.core.data import components
from epyk.mocks import urls as data_urls


# Create a basic report object
page = pk.Page()
page.headers.dev()

# Console component
c = page.ui.rich.console(
  "* This is a log section for all the events in the different buttons *", options={"timestamp": True})

#
data = page.py.requests.csv(data_urls.AIRPORT_TRAFFIC)

t1 = page.ui.titles.title("Airports")
select_data = components.select.from_records(data, column="airport")
select = page.ui.select(select_data)
select.options.showTick = True
select.options.title = "Select title"

t2 = page.ui.titles.title("Cities")
select_data = components.select.from_records(data, column="city")
multi = page.ui.select(select_data, multiple=True)
multi.options.actionsBox = False
multi.options.header = "Test Select"
multi.options.selectOnTab = True
multi.options.showTick = True

# Create a lookup object
lookupData = {"Akron-Canton Regional": [
  {"value": "A", 'text': "Example 1"},
  {"value": "B", 'text': "Example 2"}
]}
select2 = page.ui.lookup(lookupData)

# Even on a select change
select.change([
  c.dom.write(select.dom.content),
  select2.build(select.dom.content)
], empty_funcs=[
  c.dom.write("emtpy"),
])

# Even on a select change
select2.change([
  # Deselect all the items
  multi.js.deselectAll(),

  # Show the different items available to identify the selected items
  c.dom.write("===="),
  c.dom.write(select2.dom.text),
  c.dom.write(select2.dom.val, stringify=True),
  c.dom.write(select2.dom.content),
  c.dom.write(select2.dom.index),
])

# Show the selected value of the component
# The selected value will be the value and not the text visible
bt1 = page.ui.button("Get Multi Select").click([
  c.dom.write(multi.dom.content),
])

# Set the selection to two items
bt2 = page.ui.button("Set Chicago and Asheville").click([
  multi.js.val(['Chicago', 'Asheville'])
])

# Button event to transform selects
bt3 = page.ui.button("Remove Chicago").click([
  # Change the style of an item in the select
  multi.js.item("Chicago").css({"color": 'orange'}),
  multi.js.refresh(),

  # Remove a component from the select
  select.js.remove("Arcata"),
  c.dom.write("Chicago removed"),
])

t3 = page.ui.titles.title("Console Logs")
c.move()
