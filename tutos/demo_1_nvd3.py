
from epyk.core.css.themes import ThemeBlue
from epyk.core.js import std
from epyk_studio.core.Page import Report
from epyk.core.data import events


page = Report()
page.headers.dev()
page.theme = ThemeBlue.BlueGrey()

page.js.customFile("FR.js", r"http://pypl.github.io/PYPL")

title = page.ui.title("PYPL PopularitY of Programming Language")
items = page.ui.inputs.autocomplete(placeholder="select a language and press enter", options={"select": True})

cols_keys = page.ui.lists.drop(html_code="cols_agg_keys")
cols_keys.style.css.min_height = 20
cols_keys.items_style(style="bullets")
cols_keys.drop()

button = page.ui.buttons.colored("Display")
button.style.css.margin_top = 5

items.options.on_select([
  cols_keys.dom.add(events.value),
  button.dom.events.trigger("click")
])

line = page.ui.charts.nvd3.line(x_axis="Date", profile=True)

tag = page.ui.rich.powered()
tag.style.css.margin_bottom = 5
tag.style.css.margin_top = 5

box = page.studio.containers.box()
box.extend([title, tag, items, cols_keys, button, line])
box.style.standard()

items.enter([cols_keys.dom.add(items.dom.content), items.dom.empty()])

button.click([
  std.var("graphData").fromArrayToRecord().setVar("records"),
  line.build(std.var("records"), options={"y_columns": cols_keys.dom.content, "x_axis": "Date"})
])

page.body.onReady([items.js.source(std.var("graphData")[0])])
