from epyk_studio.core.Page import Report
from epyk.core.css.themes import ThemeBlue
from epyk.tests import data_urls

from datetime import datetime, timedelta

page = Report()
page.theme = ThemeBlue.BlueGrey()

data = page.py.requests.csv(data_urls.COVID_US, store_location=r"C:\tmps") # store_location to save the file locally

date = '2020-12-04'
state = 'California'

date_week = str(datetime(*[int(d) for d in date.split("-")]) - timedelta(days=20)).split()[0]

result, last_day, last_week = [], [], []
for rec in data:
  if rec["state"] == state:
    result.append(rec)
    if rec["date"] == date:
      last_day.append(rec)
    if rec["date"] == date_week:
      last_week.append(rec)

title_counties = page.ui.title("COVID per counties: %s" % date)
bar_county = page.ui.charts.chartJs.bar(last_day, y_columns=["cases", "deaths"], x_axis="county")
bar_county.options.scales.y_axis().ticks.toNumber()
bar_county.options.tooltips.callbacks.labelNumber()

title_week = page.ui.title("COVID figures: %s" % date_week)
pie_week_worst = page.ui.charts.chartJs.pie(sorted(last_week, key=lambda k: float(k['deaths']))[-5:], y_columns=["deaths"], x_axis="county")
bar_week_worst = page.ui.charts.chartJs.bar(sorted(last_week, key=lambda k: float(k['deaths']))[-min(len(last_week), 15):], y_columns=["cases", "deaths"], x_axis="county")
pie_week_worst.options.tooltips.callbacks.labelNumber()
bar_week_worst.options.scales.y_axis().ticks.toNumber()
bar_week_worst.options.tooltips.callbacks.labelNumber()

title_current = page.ui.title("COVID figures: %s" % date)
pie_worst = page.ui.charts.chartJs.pie(sorted(last_day, key=lambda k: float(k['deaths']))[-5:], y_columns=["deaths"], x_axis="county")
bar_worst = page.ui.charts.chartJs.bar(sorted(last_day, key=lambda k: float(k['deaths']))[-min(len(last_week), 15):], y_columns=["cases", "deaths"], x_axis="county")
pie_worst.options.tooltips.callbacks.labelNumber()
bar_worst.options.scales.y_axis().ticks.toNumber()
bar_worst.options.tooltips.callbacks.labelNumber()

row_week = page.ui.row([pie_week_worst, bar_week_worst])
row_week.set_size_cols(3)
row = page.ui.row([pie_worst, bar_worst])
row.set_size_cols(3)

title_histo = page.ui.title("COVID History")
bar = page.ui.charts.chartJs.line(result, y_columns=["cases", "deaths", "fips"], x_axis="date")
bar.options.scales.y_axis().ticks.toNumber()
bar.options.stacked = True
bar.options.tooltips.callbacks.labelNumber()

row_data = page.ui.row([
  [title_counties, bar_county],
  [title_histo, bar]
])

title_state = page.ui.titles.head(state)

# Create a container for the HTML page
box = page.studio.containers.box()
box.extend([title_state, row_data, title_current, row, title_week, row_week])
box.style.configs.doc(background=page.theme.white)
