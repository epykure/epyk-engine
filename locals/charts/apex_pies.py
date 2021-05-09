
import epyk as pk
import __init__


# Test module to get test data
from epyk.tests import data_urls


page = pk.Page()
__init__.add_banner(page, __file__)
# page.verbose = True

data = page.py.requests.csv(data_urls.COVID_US, store_location=r"C:\tmps") # store_location to save the file locally

dates = set()
for rec in data:
  dates.add(rec['date'])

last_day = sorted(list(dates))[-1]

f_data = []
for rec in data:
  if rec["date"] == last_day:
    f_data.append(rec)

page.ui.title("USA Covid cases")
page.ui.text("Date: %s" % last_day)
usa_map = page.ui.geo.jqv.usa(f_data, "cases", "state")

chart_deaths = page.ui.charts.apex.pie(sorted(f_data, key=lambda k: k['deaths'])[-10:], "deaths", 'state', height=200)
chart_cases = page.ui.charts.apex.donut(sorted(f_data, key=lambda k: k['cases'])[-10:], "cases", 'state', height=200)
chart_cases.options.theme.monochrome.enabled = True
#chart_cases.options.plotOptions.radialBar.dataLabels.position = "top"

page.ui.row([usa_map, [chart_deaths, chart_cases]])
__init__.add_powered(page)
