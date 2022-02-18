
import epyk as pk
from epyk.mocks import urls as data_urls
from epyk.core.data import components


# Create a basic report object
page = pk.Page()
page.headers.dev()

# Console component
c = page.ui.rich.console(
  "* This is a log section for all the events in the different buttons *", options={"timestamp": True})

# Input data from a CSV file
data = page.py.requests.csv(data_urls.AIRPORT_TRAFFIC)

select_data = components.select.from_records(data, column="airport")
select = page.ui.select(select_data)
select.options.empty = True
select.options.all = True
select.options.selected = "Adams"

select_data = components.select.from_records(data, column="city")
select_city = page.ui.select(select_data)

select_data = components.select.from_records(data, column="state")
select_state = page.ui.select(select_data, multiple=True)

select.change([
  c.dom.write(select.dom.content),
])

select_city.change([
  c.dom.write(select_city.dom.content),
])

select_state.change([
  c.dom.write(select_state.dom.content),
])
