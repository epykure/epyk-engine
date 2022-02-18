
from epyk.core.Page import Report

from epyk.mocks import urls as data_urls

page = Report()
page.headers.dev()


# https://codepen.io/sgratzl/pen/qBWwxKP

records = [
  {"name": "France", "value": 23}
]
page.ui.geo.chartJs.choropleths.world(records, y_columns=["value"], x_axis="name")
page.ui.geo.chartJs.choropleths.us(records, y_columns=["value"], x_axis="name")
