from epyk.core.css.themes import ThemeBlue
from epyk.core.js import std
from epyk_studio.core.Page import Report


page = Report()
page.headers.dev() # Change the Epyk logo
page.theme = ThemeBlue.BlueGrey()

page.js.customFile("FR.js", r"http://pypl.github.io/PYPL")

title = page.ui.title("PYPL PopularitY of Programming Language")
items = page.ui.inputs.autocomplete(placeholder="select a language and press enter", options={"select": True})

cols_keys = page.ui.lists.drop(["Date"], html_code="cols_agg_keys")
cols_keys.style.css.min_height = 20
cols_keys.items_style(style="bullets")
cols_keys.drop()

items.enter([cols_keys.dom.add(items.dom.content), items.dom.empty()])

button = page.ui.button("Display")
button.style.css.margin_top = 5
button.style.css.margin_bottom = 5

button_all = page.ui.button("All languages")
button_all.style.css.margin_top = 5
button_all.style.css.margin_left = 20
button_all.style.css.margin_bottom = 5

table = page.ui.table()
table.config.layout.fitDataFill()
table.config.paginationSize = 10
table.style.strip()

box = page.studio.containers.box()
box.extend([title, items, cols_keys, items, button, button_all, table])
box.style.standard()

button.click([
  table.js.clearData(),
  table.js.setDataFromArray(
    std.var("graphData"), header=cols_keys.dom.content,
    formatters={"Date": "(function(data){return data['Date'].toISOString().split('T')[0]})"}),
  table.js.redraw(True),
])

button_all.click([cols_keys.dom.add(std.var("graphData")[0])])

page.body.onReady([
  items.js.source(std.var("graphData")[0])
])
