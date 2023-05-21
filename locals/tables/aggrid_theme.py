import epyk as pk


# Create a basic report object
page = pk.Page()
page.headers.dev()

page.properties.css.add_text('''
.ag-theme-mycustomtheme {
    /* customise with CSS variables */
    --ag-grid-size: 8px;
    --ag-border-color: red;
}
.ag-theme-mycustomtheme .ag-header {
    /* or with CSS selectors targeting grid DOM elements */
    font-style: italic;
}
''')

table = page.ui.tables.aggrids.table(rows=["athlete", "country", "sport", 'year'])
table.theme("ag-theme-mycustomtheme", custom_cls_name=True)
table.onReady([
    page.js.fetch("https://www.ag-grid.com/example-assets/olympic-winners.json").json().process(table.js.setRowData)])
page.outs.html_file(print_paths=True, run_id=False)