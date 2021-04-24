"""
**Simple Dashboard to render logs.**

In this onePy script, you will learn how to use FASTAPI and some basic components.
It is an interactive dashboard using a nav bar in order to filter the data to be displayed.

This tutorial will illustrate how to:
- Use some generic components from the framework.
- Use a **QRcode** to create links.
- Use templates for the page layout.
- Use CSS shortcut to customise components **qrcode.style.css.**.

This report is quite advanced as it will use some of the features available in Epyk.
Namely:
- Use CSS features from **.style.css** to change the style.
- Search component with the **enter()** event.
- **page.js.post()** to call the underlying FASTAPI server.

"""
import epyk as pk
from epyk.core.data import components


# Socket server url
SERVER_DATA_HOST = "127.0.0.1"
SERVER_DATA_PORT = 5000

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

# TODO add css object shortcut
# TODO add template to body as shortcut

app = FastAPI(debug=True)

origins = ["*", "http://%s" % SERVER_DATA_HOST, "http://localhost"]
app.add_middleware(
  CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


@app.get('/', response_class=HTMLResponse)
def home():
  return create_page().outs.html()


@app.post("/viewer")
async def get_view(request: Request):
  data = await request.json()
  return {"message": f'From {data["from"]} to {data["to"]} Type **{data["log_typ"]}** Search Value {data["search"]}'}


def create_page():
  page = pk.Page()

  qrcode = page.ui.qrcode("https://github.com/epykure/epyk-templates/blob/master/tutos/onepy/fastapi_viewer_logs.py")
  qrcode.style.css.fixed(bottom=60, right=70)
  qrcode.style.css.cursor = "pointer"
  qrcode.style.css.z_index = 300

  template = page.body.add_template(defined_style="margins")

  epyk = page.ui.icons.epyk()
  epyk.style.css.margin_right = 10

  template.style.css.padding_top = 40
  dt_from = page.ui.date(icon=False, width=120, html_code="from")
  dt_from.tooltip("From Date")
  dt_to = page.ui.date(width=120, icon=False, html_code="to")
  dt_to.tooltip("To Date")
  dt_to.style.css.margin_left = 10
  dt_to.style.css.margin_right = 10
  select = page.ui.select(
    components.select.from_list(["Info", "Debug", "Warning"]), width=(80, "px"), html_code="log_typ")
  search = page.ui.rich.search_input(width=(100, 'px'), color="white", extensible=True,
                                     options={"icon": False, "borders": "bottom"}, html_code="search")
  search.style.css.margin_left = 10
  search.input.style.css.color = "white !IMPORTANT"
  text = page.ui.text()
  button = page.ui.buttons.colored("Get")
  button.style.css.margin_left = 20
  button.style.css.padding_left = 20
  button.style.css.padding_right = 20
  search.enter([button.dom.events.trigger("click")])

  bar = page.ui.div([epyk, dt_from, dt_to, select, search, text, button])
  bar.style.css.fixed(left=0, top=0)
  bar.style.css.background = page.theme.notch()
  bar.style.css.color = "white"
  bar.components.css({"display": 'inline-block'})

  page.ui.title("log Analyzer")
  console = page.ui.rich.console(height="auto", options={"markdown": True})
  console.style.css.overflow = None

  button.click(page.js.post("/viewer", components=[dt_from, dt_to, select, search], profile=True).onSuccess([
    console.dom.write(pk.events.data["message"]),
    page.js.console.log("Log message")
  ]))
  return page


if __name__ == '__main__':
  import uvicorn

  uvicorn.run("%s:app" % __file__[:-3], host=SERVER_DATA_HOST, port=SERVER_DATA_PORT, reload=True)
