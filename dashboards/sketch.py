
import config
import json

from epyk.core.Page import Report
from epyk.core.data import events
from epyk.core.data import loops


# Create a basic report object
page = Report()
page.headers.dev()

server = page.data.js.server(
  config.SERVER_DATA_HOST, config.SERVER_DATA_PORT).endPoints(["file", "data"]).addNamespace('news', alias="name")

div = page.ui.div()

path_file = r"C:\tmps\1c7b32e2f5e9189386cd8f836bc650f987f101d4"
data = json.load(open(path_file))

#
columns = page.ui.lists.chips()
rows = page.ui.lists.chips()

#
page.ui.row([
  page.ui.col([page.ui.title("Rows"), rows]),
  page.ui.col([page.ui.title("Columns"), columns])
])

#
items = page.ui.lists.items(list(data[0].keys()))
items.draggable()

#
columns.drop([columns.dom.add(events.data)])
rows.drop([rows.dom.add(events.data)])

files = page.ui.network.dropfile()
files.drop([
  files.transfer(server.get("file")).onSuccess([
    page.js.console.log("data", skip_data_convert=True)
  ])
, events.files.forEach([
      div.dom.append(loops.file.name + ": " + loops.file.size)
    ])
] )

div.move()

