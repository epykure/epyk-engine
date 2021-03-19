
from epyk.core.data import events
from epyk.core.Page import Report
from epyk.core.data import components as cpns
from epyk.core.css.themes import ThemeBlue

from pandas_datareader import data as pddr

# Socket server url
SERVER_SOCKET_HOST = "127.0.0.1"
SERVER_SOCKET_PORT = 5000

from flask import Flask
app = Flask(__name__)


def create_page():
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
  title = page.ui.title("Flask - Advanced example 2")
  ticker = page.ui.fields.select(
    cpns.select.from_dict(tickers_info), label="Tickers", multiple=True, html_code="ticker_value")
  from_dt = page.ui.fields.date(value="M-1", html_code="from_date", label="From")
  to_dt = page.ui.fields.today(html_code="to_date", label="To")
  button = page.ui.buttons.colored("Click")
  sub_title = page.ui.title("Financial Sector")
  pivot = page.ui.tables.pivots.plotly()
  button.click([
    page.body.loading(),
    page.js.post("/test_event", components=[ticker, from_dt, to_dt]).onSuccess([
      pivot.build(events.data["table"]), page.body.loading(False)])])
  powered = page.ui.rich.powered()
  hr = page.ui.layouts.hr()
  box = page.ui.div()
  box.extend([title, powered, hr, ticker, from_dt, to_dt, button, sub_title, pivot])
  box.style.doc()
  return page


if __name__ == "__main__":
  from flask import Flask, jsonify, request

  @app.route('/')
  def ui():
    return create_page().outs.html()

  @app.route('/test_event', methods=['POST'])
  def test_event():
    data = request.get_json()
    if not data['ticker_value']:
      return jsonify({"table": []})

    agg_data = []
    for ticker in data['ticker_value']:
      s = pddr.DataReader(ticker, 'yahoo', data["from_date"], data["to_date"])
      s["Price"] = (s["Open"] + s["Close"]) / 2
      s.reset_index(level=0, inplace=True)
      for rec in s.to_dict(orient="records"):
        for c in ["Low", "High", "Close", "Open", "Volume", "Price"]:
          agg_data.append({"name": ticker, 'Date': str(rec["Date"])[:10], "type": c, "value": float(rec[c])})
    return jsonify({"table": agg_data})

  Flask.run(app, host=SERVER_SOCKET_HOST, port=SERVER_SOCKET_PORT, debug=True)
