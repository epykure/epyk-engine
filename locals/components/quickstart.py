
import epyk as pk
from epyk.mocks import randoms


# Create a basic report object
page = pk.Page()
page.headers.dev()

# Create JavaScript data
js_data = page.data.js.record(js_code="myData", data=randoms.languages)
# Add a filter object
filter1 = js_data.filterGroup("filter1")

# Add a dropdown box to drive the data changes in the charts
select = page.ui.select([
  {"value": 'name', 'name': 'name'},
  {"value": 'type', 'name': 'code'},
], options={"empty_selected": False})

# Create HTML charts
bar = page.ui.charts.chartJs.bar(randoms.languages, y_columns=["rating", 'change'], x_axis='name')
pie = page.ui.charts.chartJs.pie(randoms.languages, y_columns=['change'], x_axis='name')

# Add the charts to a row
row = page.ui.row([bar, pie])

# Add a change event on the dropdown to update the charts
select.change([
  bar.build(filter1.group().sumBy(['rating', 'change'], select.dom.content), options={"x_axis": select.dom.content}),
  pie.build(filter1.group().sumBy(['change'], select.dom.content), options={"x_axis": select.dom.content}),
])

