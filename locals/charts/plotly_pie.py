
import epyk as pk


page = pk.Page()
page.headers.dev()

pie = page.ui.charts.plotly.pie()
pie.data.values = [2, 3, 4, 4]
pie.data.type = "pie"
pie.data.textinfo = "label+percent"
pie.data.textposition = "outside"
pie.data.automargin = True
pie.data.labels = ["Wages", "Operating expenses", "Cost of sales", "Insurance"]
pie.layout.no_background()
pie.data.outsidetextfont.color = 'blue'

