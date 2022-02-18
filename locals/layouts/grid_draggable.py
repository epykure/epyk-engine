
import epyk as pk


# Create a basic report object
page = pk.Page()
page.headers.dev()

rows = []
for i in range(10):
  row = [page.ui.div("Test %s col %s" % (i, j)).css({"margin": '10px'}) for j in range(3)]
  rows.append(row)

grid = page.ui.layouts.table(rows)
sortable = grid.body.sortable(propagate_only=True)

#sortable.options.ghostClass = "sortable-ghost"
#sortable.options.handle = ".col"

div = page.ui.div("Test")
div.drop([
  div.build(pk.events.data)
])

