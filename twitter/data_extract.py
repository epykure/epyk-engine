
import epyk as pk
from epyk.tests import data_urls


page = pk.Page()
chart = page.ui.chart.line(y_columns=["Armenia", "France", "Germany"], x_axis="year")
page.body.onLoad([
  page.js.fetch(data_urls.C02_DATA).csvtoRecords().get([
    chart.build(page.data.js.record("data").filterGroup("test").pivot("country", "co2", "year", type="float"))
  ])
])
page.outs.html_file(name="outDataExtract")
