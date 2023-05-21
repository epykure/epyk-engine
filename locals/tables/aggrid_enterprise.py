
import epyk as pk


# Create a basic report object
page = pk.Page()
page.imports.pkgs.ag_grid.set_enterprise()
page.headers.dev()

table = page.ui.tables.aggrids.table(rows=["athlete", "country", "sport", 'year'])
table.theme("balham")
c = table.get_column("athlete")
c.headerCheckboxSelection = True
c.headerCheckboxSelectionCurrentPageOnly = True
c.checkboxSelection = True
c.showDisabledCheckboxes = True
table.options.rowSelection = 'multiple'
table.options.suppressRowClickSelection = True
table.onReady([
page.js.fetch("https://www.ag-grid.com/example-assets/olympic-winners.json").json().process(table.js.setRowData)
])


table = page.ui.tables.aggrids.table(rows=["country", "sport", 'gold', 'silver', 'bronze', 'age', 'year', 'date'])
table.theme("material")
table.headers({
    "country": {"rowGroup": True, "hide": True},
    "sport": {"rowGroup": True, "hide": True},
    "athlete": {"rowGroup": True, "hide": True},
    "gold": {"aggFunc": "sum"},
    "silver": {"aggFunc": "sum"},
    "bronze": {"aggFunc": "sum"},
    "age": {"minWidth": 120, "checkboxSelection": True, "aggFunc": "sum"},
    "year": {"maxWidth": 120},
    "date": {"minWidth": 150},
})

table.options.defaultColDef.flex = 1
table.options.defaultColDef.minWidth = 100
table.options.defaultColDef.filter = True
table.options.defaultColDef.resizable = True

table.options.autoGroupColumnDef.headerName = 'Athlete'
table.options.autoGroupColumnDef.field = 'athlete'
table.options.autoGroupColumnDef.cellRenderers.agGroupCellRenderer()
table.options.autoGroupColumnDef.cellRendererParams.checkbox = True
table.options.autoGroupColumnDef.minWidth = 250

table.options.rowSelection = 'multiple'
table.options.groupDefaultExpanded = -1
table.options.groupSelectsChildren = True
table.options.suppressRowClickSelection = True
table.options.suppressAggFuncInHeader = True
table.onReady([
page.js.fetch("https://www.ag-grid.com/example-assets/olympic-winners.json").json().process(table.js.setRowData)
])

page.ui.button("value").click([page.js.console.log(table.dom.selection())])

page.outs.html_file(print_paths=True, run_id=False)