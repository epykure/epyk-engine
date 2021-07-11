
import epyk as pk
from epyk.tests import data_urls

page = pk.Page()

page.body.style.css.padding_h = 10  # Add padding to the body
# get data from external github repository and create a filter group
records = page.py.requests.csv(data_urls.DEMO_COUNTRY)
grp = page.data.js.record(records).filterGroup("aggData")

title = page.ui.title()  # Add a title component
select = page.ui.fields.select(  # Add select component
  pk.inputs.select.from_records(records, column='Country Name'), label="Country")
select.input.options.liveSearch = True  # Add filter on the long select
# Add a chart (default ChartJs)
chart = page.ui.charts.line(y_columns=["Value"], x_axis="Year")
# Event when select in the field is changed
select.input.change([  # rebuild the components
  chart.build(grp.equal("Country Name", select.input.dom.content)),
  title.build(select.input.dom.content)
])
select.move()  # Move the component after the input

page.outs.html_file(name="outSelectFilter")
