
from epyk.core.Page import Report

from epyk.mocks import urls as data_urls


page = Report()
page.headers.dev()

data_countries = page.py.requests.csv(data_urls.PLOTLY_COUNTRIES)

data_geo = page.py.requests.csv(data_urls.GEO_US_CITIES)

m = page.ui.geo.plotly.bubbles.usa(
  data_geo, size_col='pop', long_col='lon', lat_col='lat', options={"scale": 50000, 'size': 1})

sa = page.ui.geo.plotly.bubbles.south_america(data_countries, size_col='GDP (BILLIONS)', country_col='CODE')
w = page.ui.geo.plotly.bubbles.world(data_countries, size_col='GDP (BILLIONS)', country_col='CODE')

page.ui.row([w, sa])

records = [
  {'location': 'GBR', 'value': 40}
]
page.ui.button("Click").click([
  #w.build(page.data.plotly.locations(data_geo, 'location', 'value'))
  w.build(page.data.plotly.locations(data_geo, 'lon', 'lat', 'pop'))
])

