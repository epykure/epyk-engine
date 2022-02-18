
from epyk.core.Page import Report
from epyk.core.data import components
from epyk.mocks import urls as data_urls


# Create a basic report object
page = Report()
page.headers.dev()


data = page.py.requests.csv(data_urls.AIRPORT_TRAFFIC)

cities = components.list.from_records(data, "city")
a = page.ui.lists.points(cities)

airports = components.list.from_records(data, "airport")
b = page.ui.lists.numbers(airports)

states = components.list.from_records(data, "state")
c = page.ui.lists.roman(states)

row = page.ui.row([a, b, c], position="top")
row.options.responsive = False
