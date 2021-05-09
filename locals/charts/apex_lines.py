
import epyk as pk
import __init__

# Test module to get test data
from epyk.tests import data_urls

page = pk.Page()
__init__.add_banner(page, __file__)

state = "California"
data = page.py.requests.csv(data_urls.COVID_US, store_location=r"C:\tmps") # store_location to save the file locally
chart = page.ui.charts.apex.line(data, ["cases"], 'state')

state_data = []
for rec in data:
  if rec["state"] == state:
    state_data.append(rec)

chart_texas = page.ui.charts.apex.line(state_data, ["cases", "deaths"], 'date')
chart_texas.options.dataLabels.enabled = False
chart_texas.options.title.text = state
chart_texas.options.subtitle.text = "Cases"
chart_texas.zoomable()

chart_county = page.ui.charts.apex.line(state_data, ["cases"], 'county')
chart_county.options.dataLabels.enabled = False
chart_texas.zoomable()

page.ui.row([chart_texas, chart_county])
__init__.add_powered(page)
