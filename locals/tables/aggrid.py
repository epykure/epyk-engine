
import epyk as pk


# Create a basic report object
page = pk.Page()
page.headers.dev()

table = page.ui.tables.aggrids.table(rows=["country", "sport", 'gold', 'silver', 'bronze', 'age', 'year', 'date'])
table.theme("alpine")

table.onReady([
page.js.fetch("https://www.ag-grid.com/example-assets/olympic-winners.json").json().process(table.js.setRowData)
])
page.outs.html_file(print_paths=True, run_id=False)