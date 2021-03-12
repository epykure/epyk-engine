
from epyk.core.data import events
from epyk.core.Page import Report
from epyk.core.data import components as cpns
from epyk.core.css.themes import ThemeBlue
from epyk.core.data import chartJs

from pandas_datareader import data as pddr
from functools import reduce
import pandas as pd

# Socket server url
SERVER_SOCKET_HOST = "127.0.0.1"
SERVER_SOCKET_PORT = 5000

from flask import Flask
app = Flask(__name__)


def get_page_flask():
  page = Report()
  page.headers.dev()
  page.theme = ThemeBlue.BlueGrey()

  tickers_info = {
    'BAC': "Bank of America",
    'GS': "Goldman Sachs",
    'JPM': "JPMorgan Chase",
    'SAN.MC': "Banco Santander",
    'C.MX': "Citigroup Inc.",
    'HSBC-PA': "HSBC Holdings PLC"
  }
  title = page.ui.title("Flask - Advanced example 1")
  ticker = page.ui.fields.select(
    cpns.select.from_dict(tickers_info), label="Tickers", multiple=True, html_code="ticker_value")
  from_dt = page.ui.fields.date(value="M-1", html_code="from_date", label="From")
  to_dt = page.ui.fields.today(html_code="to_date", label="To")
  button = page.ui.buttons.colored("Click")
  text = page.ui.calendars.pill("1Y", group="chart_time")
  text_6m = page.ui.calendars.pill("6M", group="chart_time")
  text_2m = page.ui.calendars.pill("2M", group="chart_time")
  text_1m = page.ui.calendars.pill("1M", group="chart_time")
  sub_title = page.ui.title("Financial Sector 2020")
  buttons = page.ui.div([text, text_6m, text_2m, text_1m])
  chart = page.ui.charts.chartJs.line([], x_axis='Date')
  chart.options.scales.y_axis().ticks.toNumber()
  chart.options.scales.y_axis().add_label("Stock Price (USD)")
  chart.options.scales.x_axes().add_label("Date")
  chart.options.tooltips.callbacks.labelCurrency("$", digit=4)

  table = page.ui.tables.aggrid([])
  button.click([
    page.body.loading(),
    page.js.post("/test_event", components=[ticker, from_dt, to_dt]).onSuccess([
      chart.build(events.data["chart"]), table.js.setColumnDefs(events.data["columns"]),
      table.js.setRowData(events.data["table"]), page.body.loading(False)])])
  text.click([from_dt.input.build(text.dom.content), button.dom.events.trigger("click")])
  text_6m.click([from_dt.input.build(text_6m.dom.content), button.dom.events.trigger("click")])
  text_2m.click([from_dt.input.build(text_2m.dom.content), button.dom.events.trigger("click")])
  text_1m.click([from_dt.input.build(text_1m.dom.content), button.dom.events.trigger("click")])
  powered = page.ui.rich.powered()
  hr = page.ui.layouts.hr()
  box = page.ui.div()
  box.extend([title, powered, hr, ticker, from_dt, to_dt, button, sub_title, buttons, chart, table])
  box.style.doc()
  return page


if __name__ == "__main__":
  from flask import Flask, jsonify, request

  @app.route('/')
  def ui():
    return get_page_flask().outs.html()

  @app.route('/test_event', methods=['POST'])
  def test_event():
    data = request.get_json()
    if not data['ticker_value']:
      return jsonify({'chart': chartJs.y(None, data['ticker_value'], "Date"), "table": [], "columns": []})

    series, agg_data = [], []
    for ticker in data['ticker_value']:
      s = pddr.DataReader(ticker, 'yahoo', data["from_date"], data["to_date"])
      s[ticker] = (s["Open"] + s["Close"]) / 2
      s["name"] = ticker
      prices = s[[ticker]]
      prices.reset_index("Date")
      series.append(prices)
      agg_data.append(s)
    series = reduce(lambda df1, df2: pd.merge(df1, df2, on='Date'), series)
    concat_series = reduce(lambda df1, df2: pd.merge(df1, df2, on='Date'), agg_data)
    concat_series.reset_index(level=0, inplace=True)
    records = []
    for rec in series[data['ticker_value']].to_records():
      records.append(dict(zip(['Date'] + data['ticker_value'], rec)))
      records[-1]['Date'] = pd.to_datetime(records[-1]['Date']).strftime('%Y-%m-%d')
    return jsonify({'chart': chartJs.y(records, data['ticker_value'], "Date"),
                    "table": concat_series.to_dict(orient="records"),
                    "columns": [
                       {"headerName": "Date", "field": "Date"},
                       {"headerName": "Ticker", "field": "name"},
                       {"headerName": 'Low', "field": 'Low'},
                       {"headerName": 'High', "field": 'High'},
                       {"headerName": 'Open', "field": 'Open'},
                       {"headerName": 'Close', "field": 'Close'},
                       {"headerName": 'Volume', "field": 'Volume'},
                    ]})

  Flask.run(app, host=SERVER_SOCKET_HOST, port=SERVER_SOCKET_PORT, debug=True)
