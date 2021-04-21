
import epyk as pk


# Socket server url
SERVER_DATA_HOST = "127.0.0.1"
SERVER_DATA_PORT = 5000

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI(debug=True)

import time
import json
import os

from selenium import webdriver
from bs4 import BeautifulSoup


@app.get('/', response_class=HTMLResponse)
def home():
  return create_page().outs.html()


@app.post("/web_scrapping")
async def get_prices(request: Request):
  data = await request.json()
  page = pk.Page()
  dates = page.py.dates.range_dates(data["from"], data["to"])
  prices, averages = [], {}
  driver = webdriver.Firefox(executable_path=r"C:\servers\browsers\geckodriver.exe")
  for date in dates:
    tmp_file = os.path.join("C:/tmps", "eurostar_%s.json" % date.replace("-", ""))
    if not os.path.exists(tmp_file):
      url = 'https://booking.eurostar.com/uk-en/train-search?origin=7015400&destination=8727100&adult=1&outbound-date=%s' % date
      driver.get(url)
      time.sleep(3)
      content = driver.page_source
      soup = BeautifulSoup(content, features="lxml")
      results, row = [], {}
      categories = ['standard', 'premier', 'business']
      for i, t in enumerate(soup.find_all("section", {'class': 'train__class-of-accommodation'})):
        if i % 3 == 0 and row:
          results.append(row)
          row = {}
        if t.find("div", {"class": 'coa__price-container'}) is None:
          row[categories[i % 3]] = None
        else:
          row[categories[i % 3]] = t.find("div", {"class": 'coa__price-container'}).find("span", {
            "class": 'price price--gbp'}).text
      results.append(row)
      for i, t in enumerate(soup.find_all("section", {'class': 'journey-details'})):
        results[i]['time'] = t.find("li", {'class': 'item-depart'}).text
        results[i]['date'] = date
      with open(tmp_file, "w") as f:
        json.dump(results, f)
    else:
      with open(tmp_file) as f:
        results = json.load(f)
    for rec in results:
      if 'time' in rec:
        rec['full_date'] = "%s %s" % (date, rec['time'])
        for p in ['standard', 'premier', 'business']:
          rec[p] = float(rec[p][1:]) if rec[p] is not None else rec[p]
          if p not in averages:
            averages[p] = {"sum": 0, "count": 0}
          averages[p]["sum"] += rec[p]
          averages[p]["count"] += 1
    prices.extend(results)
  driver.quit()
  return {"prices": prices[::-1],
          "average": [{"category": k, "average": v["sum"] / v["count"]}for k, v in averages.items()]}


def create_page():
  page = pk.Page()
  page.body.template.style.configs.margins()

  qrcode = page.ui.qrcode("https://github.com/epykure/epyk-templates/blob/master/tutos/onepy/fastapi_viewer_logs.py")
  qrcode.style.css.fixed(bottom=60, right=70)
  qrcode.style.css.cursor = "pointer"
  qrcode.style.css.z_index = 300
  
  dt_from = page.ui.date(html_code='from', width=(120, "px"))
  dt_from.input.style.css.margin_bottom = 10
  dt_to = page.ui.date("2021-05-15", html_code='to', width=(120, "px"))
  dt_to.input.style.css.margin_bottom = 10
  prices = page.ui.button("Get Prices", icon="fab fa-python")
  prices.style.css.padding_left = 10
  prices.style.css.padding_right = 10
  prices.style.css.color = page.theme.colors[-1]
  bar = page.ui.navbar()
  bar.style.css.background = page.theme.colors[-1]
  bar.style.css.color = "white"
  bar.add(dt_from)
  bar.add(dt_to)
  bar.add(prices)
  page.ui.title("Eurostar average prices")
  line = page.ui.charts.chartJs.line(y_columns=['standard', 'premier', 'business'], x_axis='full_date')
  bar = page.ui.charts.chartJs.bar(y_columns=['average'], x_axis='name')
  row = page.ui.row([line, bar])
  row.set_size_cols(8)
  prices.click([
    prices.icon.dom.spin(True),
    page.js.post("/web_scrapping", components=[dt_from, dt_to]).onSuccess([
      line.build(pk.events.data["prices"]),
      bar.build(pk.events.data["average"]),
      prices.icon.dom.spin(False)
    ])
  ])
  return page


if __name__ == '__main__':
  import uvicorn

  uvicorn.run("%s:app" % __file__[:-3], host=SERVER_DATA_HOST, port=SERVER_DATA_PORT, reload=True)


