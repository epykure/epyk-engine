
import epyk as pk


# Create a basic report object
page = pk.Page()
page.imports.pkgs.ag_grid.set_enterprise()
page.headers.dev()


table = page.ui.tables.aggrids.table(html_code="table_test")
date = page.ui.date()
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

page.ui.button("update").click([
    page.js.fetch("https://www.ag-grid.com/example-assets/olympic-winners.json").json().process(table.js.setRowData)
])

page.ui.button("cache").click([
    page.js.localStorage.getItem("%s_headers" % table.html_code).jsonParse(),
    table.js.setColumnDefs(page.js.localStorage.getItem("%s_headers" % table.html_code).jsonParse()),
    table.js.setRowData(page.js.localStorage.getItem("%s_rows" % table.html_code).jsonParse())
])

page.ui.button("store").click([
    page.js.console.log(table.js.getColumnDefs()),
    page.js.localStorage.setItem("%s_rows" % table.html_code, table.js.getRowsData().stringify()),
    page.js.localStorage.setItem("%s_headers" % table.html_code, table.js.getColumnDefs().stringify())
])

js_request = page.js.post("https://www.ag-grid.com/example-assets/olympic-winners.json", components=[date],
                         data={"test": "It works!"}, dataflows=[
        {"name": "(function(r){console.log(r); return r})"}
    ])
page.ui.button("post").click([
    js_request.onSuccess([page.js.console.log(js_request.URL)
    ]).onerror([page.js.console.log(js_request.URL)])
])
page.outs.html_file(print_paths=True, run_id=False)
