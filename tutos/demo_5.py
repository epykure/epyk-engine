from epyk_studio.core.Page import Report
from epyk.core.css.themes import ThemeBlue

import pandas as pd
from pandas_datareader import data

start = pd.to_datetime('2020-02-04')
end = pd.to_datetime('today')

tesla_df = data.DataReader('TSLA', 'yahoo', start, end)

columns = ['Close', 'Open', 'Volume']
records = []
for rec in tesla_df[columns].to_records():
  records.append(dict(zip(['Date'] + columns, rec)))
  records[-1]['Date'] = pd.to_datetime(records[-1]['Date']).strftime('%Y-%m-%d')

page = Report()
page.theme = ThemeBlue.BlueGrey()

from_dt = page.ui.fields.date(value=None, html_code="from_date", label="From")
to_dt = page.ui.fields.date(value=None, html_code="to_date", label="To")

button = page.ui.buttons.colored("Update")

text = page.ui.calendars.pill("1Y", group="chart_time")
text_6m = page.ui.calendars.pill("6M", group="chart_time")
text_2m = page.ui.calendars.pill("2M", group="chart_time")
text_1m = page.ui.calendars.pill("1M", group="chart_time")
text_all = page.ui.calendars.pill("All", group="chart_time")

title = page.ui.title("Tesla Share Price")

buttons = page.ui.div([text, text_6m, text_2m, text_1m, text_all])

chart = page.ui.charts.chartJs.line([], y_columns=columns, x_axis='Date')
chart.options.scales.y_axis().ticks.scale(1000)
chart.options.scales.y_axis().add_label("Stock Price (USD)")
chart.options.scales.x_axes().add_label("Date")
chart.options.tooltips.callbacks.labelCurrency("$")

grp = page.data.js.record(records).filterGroup("aggData")

text.click([from_dt.input.build(text.dom.content), button.dom.events.trigger("click")])
text_6m.click([from_dt.input.build(text_6m.dom.content), button.dom.events.trigger("click")])
text_2m.click([from_dt.input.build(text_2m.dom.content), button.dom.events.trigger("click")])
text_1m.click([from_dt.input.build(text_1m.dom.content), button.dom.events.trigger("click")])
text_all.click([from_dt.input.build(records[0]["Date"]), chart.build(grp)])

box = page.studio.containers.box()
box.extend([title, from_dt, to_dt, button, page.ui.layouts.hr(margins=5), buttons, chart])
box.style.standard()

button.click([
  text.dom.classList.select(False),
  text_all.dom.classList.select(False),
  text_2m.dom.classList.select(False),
  text_1m.dom.classList.select(False),
  text_6m.dom.classList.select(False),
  chart.build(grp.sup("Date", from_dt.dom.content).inf("Date", to_dt.dom.content).group().sumBy(columns, ['Date']))
])