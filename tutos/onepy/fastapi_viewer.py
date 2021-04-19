
import epyk as pk
import pandas_datareader as pdr
import pandas as pd
from datetime import datetime


# Socket server url
SERVER_DATA_HOST = "127.0.0.1"
SERVER_DATA_PORT = 5000

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI(debug=True)

origins = ["*", "http://127.0.0.1", "http://localhost"]
app.add_middleware(
  CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


@app.get('/', response_class=HTMLResponse)
def home():
  return create_page().outs.html()


@app.post("/viewer")
async def get_view(request: Request):
  data = await request.json()
  results = pdr.DataReader(data["input"], 'yahoo',
     start=datetime(*map(lambda x: int(x), data["date_from"].split("-"))),
     end=datetime(*map(lambda x: int(x), data["date_to"].split("-"))))
  results = results.reset_index()
  results['Date'] = pd.to_datetime(results['Date']).dt.strftime('%Y-%m-%d')
  results['Name'] = data["input"]
  return {"table": results.to_dict(orient="records"), "title": " from %(date_from)s to %(date_to)s" % data}


def create_page():
  page = pk.Page()
  template = page.body.add_template(defined_style="margins")
  template.style.css.background = "white"

  dt = page.ui.texts.date("Y-0", html_code='date_from', width=(100, "%"))
  page.ui.navigation.shortcut([
    page.ui.layouts.hr(),
    page.ui.titles.title("Dates"),
    page.ui.titles.bold("From:", align="left"),
    dt,
    page.ui.titles.bold("To:", align="left"),
    page.ui.texts.date(html_code='date_to', width=(100, "%"), options={"date_from_js": "COB"}),
    page.ui.layouts.hr(),
    page.ui.titles.title("Actions"),
    page.ui.input("GS", html_code="input"),
    page.ui.buttons.refresh("Load", html_code="button"),
    page.ui.icons.date(),
    page.ui.div([
      page.ui.icons.awesome("far fa-file-pdf", width=15),
      page.ui.icons.awesome("fas fa-at", width=15),
    ]).css({"bottom": '10px', 'position': 'absolute', 'display': 'block'})
  ], size=(100, 'px'), options={"position": 'left'})

  page.body.style.css.margin_left = 10
  content = ""
  title = page.ui.title(content, options={"markdown": True})
  table = page.ui.tables.tabulators.figures(
    rows=["Date", "Name"], cols=["Low", "High", 'Open', 'Close', 'Volume', 'Adj Close'])

  footer = page.ui.navigation.footer('@Data from pandas_datareader using yahoo as source.')

  page.components['button'].click([
    page.components["button"].icon.dom.pulse(True),
    page.js.post("/viewer", {"button": 'Data 1'}, components=[page.components["input"],
      page.components['date_from'], page.components['date_to']]).onSuccess([
      title.build(pk.events.data["title"]),
      table.build(pk.events.data["table"]),
      page.components["button"].icon.dom.pulse(False)
    ]),
  ])
  page.components["input"].enter([page.components['button'].dom.events.trigger("click")])
  footer.style.css.padding_left = 110
  return page


if __name__ == '__main__':
  import uvicorn

  uvicorn.run("%s:app" % __file__[:-3], host=SERVER_DATA_HOST, port=SERVER_DATA_PORT, reload=True)
