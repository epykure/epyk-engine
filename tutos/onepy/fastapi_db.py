"""
**Rich Interactive & Editable Documentation Viewer.**

In this onePy script, you will learn how to use **FASTAPI** and **SQLite3** with an interactive web dashboard.
This tutorial will illustrate how to:
- Add components to a dashboard.
- Use event to interact with _REST API_ of an underlying server.
- Create bespoke **CssInline** styles.
- Make very quickly customisable web one pager to show to clients.

This report is quite advanced as it will use most of the features available in Epyk.
Namely:
- **pk.Page()** for the creation of a web page.
- **page.js.post()** for the POST AJAX calls.
- **pk.CssInline()** for CSS inline definition
- **page.body.onReady()** to create on Document ready event.
"""

import epyk as pk

# Socket server url
SERVER_DATA_HOST = "127.0.0.1"
SERVER_DATA_PORT = 5000

import os
import sqlite3

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI(debug=True)

origins = ["*", "http://127.0.0.1", "http://localhost"]
app.add_middleware(
  CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


# Section dedicated to the Database connection.
DB_PATH = os.path.relpath(os.path.join("..", "..", "static", "assets", 'fastapi_db.db'))
if not os.path.exists(DB_PATH):
  import importlib

  DB_CONN = sqlite3.connect(DB_PATH)
  DB_CONN.execute('''CREATE TABLE scripts (name text, title text, dsc text, version text, date text)''')
  scripts = {"fastapi_viewer": "Documentation Viewer", "fastapi_viewer_logs": "Log Analyser",
             "fastapi_webscraping": "Web data extraction"}
  for script, title in scripts.items():
    mod = importlib.import_module(script)
    cur = DB_CONN.cursor()
    inputs = {"script": "%s.py" % script, "title": title, "content": mod.__doc__, "version": "0.0.0", "last_update": ""}
    cur.execute(
      "INSERT INTO scripts VALUES ('%(script)s', '%(title)s', '%(content)s', '%(version)s', '%(last_update)s')" % inputs)
    DB_CONN.commit()

else:
  DB_CONN = sqlite3.connect(DB_PATH)


# Section dedicated to the FASTAPI entry points.
@app.get('/', response_class=HTMLResponse)
def home():
  return create_page().outs.html()


@app.post("/details")
async def get_details(request: Request):
  inputs = await request.json()
  inputs["version"] = inputs["selected_version"].replace("\\", "")
  rec = []
  for rec in DB_CONN.execute(
    "select name, title, dsc, version, date FROM scripts WHERE name='%(name)s' AND version='%(version)s'" % inputs):
    pass
  if not rec:
    return {"title": "", "content": "", "number": "", "script": ""}
  return {"title": rec[1], "content": rec[2], "number": inputs["version"], "script": rec[0], "last_date": rec[4]}


@app.post("/templates")
async def get_templates():
  values = [{"value": row[0]} for row in DB_CONN.execute('SELECT distinct(name) FROM scripts')]
  return {"values": values}


@app.post("/versions")
async def get_versions(request: Request):
  inputs = await request.json()
  if not inputs.get('name', ''):
    return {"versions": [], "status": 'Missing name'}

  values = [{"value": row[0]} for row in DB_CONN.execute(
    'SELECT distinct(version) FROM scripts WHERE name = "%s"' % inputs["name"])]
  return {"versions": values, "status": 'Version updated', "selected": values[-1]["value"]}


@app.post("/save")
async def get_save(request: Request):
  inputs = await request.json()
  inputs["version"] = inputs["version"].replace("\\", "")
  inputs["script"] = inputs["script"].replace("\\", "")
  print(inputs)
  cur = DB_CONN.cursor()
  cur.execute(
    "INSERT INTO scripts VALUES ('%(script)s', '%(title)s', '%(content)s', '%(version)s', '%(last_update)s')" % inputs)
  DB_CONN.commit()
  return {"status": "config saved"}


# Section dedicated to render the rich and interactive UI.
# This will be generated by the home route and then it will interact with the other routes from the component events.
def create_page():
  page = pk.Page()

  css = pk.CssInline()
  css.margin_bottom = 5
  css.margin_left = 5
  css.important(["margin_bottom", "margin_left"])

  autocomp = page.ui.inputs.autocomplete(placeholder="script name", html_code="name", options={"borders": "bottom"})
  autocomp.options.select = True
  version = page.ui.select(width=(100, 'px'), html_code="selected_version")
  version.attr["class"].add(css.to_class("cssTestClass"))
  version.options.noneSelectedText = "None"
  button = page.ui.buttons.colored("Load")
  button.style.css.margin_left = 10

  page.ui.navbar(components=[autocomp, version, button])

  script = page.ui.text("script name", html_code="script")
  script.options.editable = True
  script.style.css.bold()
  pkg_version = page.ui.text("Version")
  pkg_number = page.ui.text("0.0.0", html_code="version")
  pkg_number.options.editable = True
  pkg_number.style.css.margin_left = 10
  v = page.ui.div([pkg_version, pkg_number], width="auto")
  v.style.css.float = "right"
  v.style.css.display = "inline-block"

  i1 = page.ui.icon("fas fa-edit")
  i2 = page.ui.icon("fas fa-lock")
  i3 = page.ui.icon("fas fa-save")
  actions = page.ui.div([i1, i2, i3], width=(20, 'px'))
  actions.style.css.position = "absolute"
  actions.style.css.top = 60
  actions.style.css.right = 0
  actions.style.css.padding_left = "3px"
  actions.style.css.border_radius = "5px 0 0 5px"
  actions.style.css.background = page.theme.greys[3]

  header = page.ui.div([script, v])
  header.style.css.background = page.theme.greys[2]
  header.style.css.display = "block"
  header.style.css.padding_h = 15

  title = page.ui.title("Documentation Viewer", html_code="title")
  title.options.editable = True
  content = page.ui.rich.markdown(__doc__, html_code="content")
  content.options.editable = True

  banner = page.ui.text("Editable", width=(75, 'px'))
  banner.style.css.background = page.theme.success[1]
  banner.style.css.border_radius = "0 0 20px 0"
  banner.style.css.padding_h = 10
  banner.style.css.font_factor(-2)
  banner.style.css.color = page.theme.greys[-1]
  banner.style.css.position = "absolute"
  banner.style.css.bold()
  banner.style.css.top = 0
  banner.style.css.left = 0

  container = page.ui.div([banner, header, title, content, actions])
  container.style.configs.doc(background="white")
  container.style.css.position = "relative"
  container.style.css.padding_top = 30

  updt = page.ui.rich.update(align="right", html_code="last_update")
  updt.style.css.italic()
  updt.style.css.font_factor(-2)
  container.add(updt)

  i3.click([
    page.js.post("/save", components=[banner, script, pkg_number, title, content, updt]).onSuccess([
      page.js.msg.status(),
      updt.refresh()
    ])
  ])

  i1.click([
    script.dom.setAttribute("contenteditable", True).r,
    pkg_number.dom.setAttribute("contenteditable", True).r,
    title.dom.setAttribute("contenteditable", True).r,
    content.dom.setAttribute("contenteditable", True).r,
    page.js.msg.text("Components editable"),
    banner.build("Editable"),
    banner.dom.css({"background": page.theme.success[1], "color": page.theme.greys[-1]})
  ])

  i2.click([
    script.dom.setAttribute("contenteditable", False).r,
    pkg_number.dom.setAttribute("contenteditable", False).r,
    title.dom.setAttribute("contenteditable", False).r,
    content.dom.setAttribute("contenteditable", False).r,
    page.js.msg.text("Components locked"),
    banner.build("Locked"),
    banner.dom.css({"background": page.theme.colors[-1], "color": page.theme.greys[0]})
  ])

  autocomp.enter([
    page.js.post("/versions", components=[autocomp]).onSuccess([
      version.build(pk.events.data["versions"]),
      version.js.val(pk.events.data["selected"]),
      version.js.refresh(),
      page.js.msg.status()
    ])
  ])

  button.click([
    page.js.post("/details", components=[autocomp, version]).onSuccess([
      title.build(pk.events.data["title"]),
      content.build(pk.events.data["content"]),
      script.build(pk.events.data["script"]),
      pkg_number.build(pk.events.data["number"]),
      updt.build(pk.events.data["last_date"]),
    ])
  ])
  page.body.onReady([
    page.js.post("/templates").onSuccess([
      autocomp.js.source(pk.events.data["values"])
    ])
  ])
  return page


if __name__ == '__main__':
  import uvicorn

  uvicorn.run("%s:app" % __file__[:-3], host=SERVER_DATA_HOST, port=SERVER_DATA_PORT, reload=True)