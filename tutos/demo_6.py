from epyk_studio.core.Page import Report
from epyk.core.css.themes import ThemeBlue

from functools import reduce
import pandas as pd
from pandas_datareader import data


start = pd.to_datetime('2020-02-04')
end = pd.to_datetime('today')

tickers_info = {
  'BAC': "Bank of America",
  'GS': "Goldman Sachs",
  'JPM': "JPMorgan Chase",
  'SAN.MC': "Banco Santander",
  'C.MX': "Citigroup Inc.",
  'HSBC-PA': "HSBC Holdings PLC"
}

tickers = list(tickers_info.keys())

series = []
for t in tickers:
  s = data.DataReader(t, 'yahoo', start, end)
  s[t] = (s["Open"] + s["Close"]) / 2
  prices = s[[t]]
  prices.reset_index("Date")
  series.append(prices)

series = reduce(lambda df1, df2: pd.merge(df1, df2, on='Date'), series)

records = []
for rec in series[tickers].to_records():
  records.append(dict(zip(['Date'] + tickers, rec)))
  records[-1]['Date'] = pd.to_datetime(records[-1]['Date']).strftime('%Y-%m-%d')

page = Report()
page.theme = ThemeBlue.BlueGrey()


from_dt = page.ui.fields.date(value="M-1", html_code="from_date", label="From")
to_dt = page.ui.fields.today(html_code="to_date", label="To")

button = page.ui.buttons.colored("Update")

text = page.ui.calendars.pill("1Y", group="chart_time")
text_6m = page.ui.calendars.pill("6M", group="chart_time")
text_2m = page.ui.calendars.pill("2M", group="chart_time")
text_1m = page.ui.calendars.pill("1M", group="chart_time")
text_all = page.ui.calendars.pill("All", group="chart_time")

title = page.ui.title("Financial Sector 2020")

buttons = page.ui.div([text, text_6m, text_2m, text_1m, text_all])

chart = page.ui.charts.chartJs.line([], y_columns=tickers, x_axis='Date')
chart.options.scales.y_axis().ticks.toNumber()
chart.options.scales.y_axis().add_label("Stock Price (USD)")
chart.options.scales.x_axes().add_label("Date")
chart.options.tooltips.callbacks.labelCurrency("$", digit=4)

grp = page.data.js.record(records).filterGroup("aggData")

select = page.ui.fields.select([{'name': v, 'value': k, "selected": True} for k, v in tickers_info.items()], label="Companies", multiple=True, options={"empty_selected": False})

text.click([from_dt.input.build(text.dom.content), button.dom.events.trigger("click")])
text_6m.click([from_dt.input.build(text_6m.dom.content), button.dom.events.trigger("click")])
text_2m.click([from_dt.input.build(text_2m.dom.content), button.dom.events.trigger("click")])
text_1m.click([from_dt.input.build(text_1m.dom.content), button.dom.events.trigger("click")])
text_all.click([from_dt.input.build(records[0]["Date"]), chart.build(grp, options={"y_columns": select.input.dom.content, "x_axis": "Date"})])

box = page.studio.containers.box()
box.extend([title, select, from_dt, to_dt, button, page.ui.layouts.hr(margins=5), buttons, chart])
box.style.standard()

select.input.change([button.dom.events.trigger("click")])

button.click([
  text.dom.classList.select(False),
  text_all.dom.classList.select(False),
  text_2m.dom.classList.select(False),
  text_1m.dom.classList.select(False),
  text_6m.dom.classList.select(False),
  page.js.console.log(select.dom.content),
  chart.build(grp.sup("Date", from_dt.dom.content).inf("Date", to_dt.dom.content).group().sumBy(tickers, ['Date']),
              options={"y_columns": select.input.dom.content, "x_axis": "Date"})
])


