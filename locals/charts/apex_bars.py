
import epyk as pk
import __init__

from epyk.core.js.libs import apexchart

# Test module to get test data
from epyk.tests import data_urls

page = pk.Page()
__init__.add_banner(page, __file__)

state = "Texas"
county = "Harris"

data = page.py.requests.csv(data_urls.COVID_US, store_location=r"C:\tmps") # store_location to save the file locally

chart = page.ui.charts.apex.bar(data, ["cases"], 'state')
chart.options.dataLabels.enabled = False
chart.options.yaxis.labels.formatters.scale(1000, "k$")
chart.options.yaxis.tickAmount = 2
chart.options.xaxis.labels.formatters.mapTo({"California": 'Test'})

chart.click([
  page.js.console.log("event", skip_data_convert=True),
  page.js.console.log("config", skip_data_convert=True),
  page.js.console.log(apexchart.x, skip_data_convert=True),
  page.js.console.log(apexchart.y, skip_data_convert=True)
])


state_data, county_data = [], []
for rec in data:
  if rec["state"] == state:
    state_data.append(rec)
  if rec["county"] == county:
    county_data.append(rec)

chart_texas = page.ui.charts.apex.area(state_data, ["cases", "deaths"], 'date')
chart_texas.options.dataLabels.enabled = False
chart_texas.options.title.text = state
chart_texas.options.subtitle.text = "Cases"
chart_texas.options.chart.events.custom_config("beforeResetZoom", "function(chartContext, config) { console.log('ok')}", True)

chart_harris = page.ui.charts.apex.area(county_data, ["cases", "deaths"], 'date')
chart_harris.options.dataLabels.enabled = False
chart_harris.options.title.text = county
chart_harris.options.subtitle.text = "Cases"

chart_county = page.ui.charts.apex.hbar(state_data, ["cases"], 'county', height=700)
chart_county.options.dataLabels.enabled = False

page.ui.row([[chart_texas, chart_harris], chart_county], position="top")

__init__.add_powered(page)