
from epyk.core.Page import Report
from epyk.mocks import randoms


# Create a basic report object
page = Report()
page.headers.dev()

#
page.imports.google_products(['charts'])
# The input data from https://developers.google.com/chart/interactive/docs/gallery/areachart
data = [['Year', 'Sales', 'Expenses'], ['2013', 1000, 400], ['2014', 1170, 460], ['2015', 660, 1120], ['2016', 1030, 540]]

map = page.ui.charts.google.line(randoms.languages, y_columns=["rating", 'change'], x_axis='name')

page.ui.button("Click").click([
  map.build({
    'series': ["A", 'B'],
    'x': 'x',
    'datasets': [['0', 1, 4], ['1', 2, 6]]
  })
])
