
from epyk.core.Page import Report
from epyk.mocks import urls as data_urls


page = Report()
page.headers.dev()


records = [
  {'countries': 'FRA', 'size': 20},
  {'countries': 'GBR', 'size': 50},
  {'countries': 'DEU', 'size': 30},
  {'countries': 'RUS', 'size': 15},
  {'countries': 'ESP', 'size': 15},
]


data_countries = page.py.requests.csv(data_urls.PLOTLY_COUNTRIES)

europe = page.ui.geo.plotly.choropleths.europe(data_countries, size_col='GDP (BILLIONS)', country_col='CODE')
asia = page.ui.geo.plotly.choropleths.asia(data_countries, size_col='GDP (BILLIONS)', country_col='CODE')
africa = page.ui.geo.plotly.choropleths.africa(data_countries, size_col='GDP (BILLIONS)', country_col='CODE')
sa = page.ui.geo.plotly.choropleths.south_america(data_countries, size_col='GDP (BILLIONS)', country_col='CODE')
na = page.ui.geo.plotly.choropleths.north_america(data_countries, size_col='GDP (BILLIONS)', country_col='CODE', height=(600, 'px'))

page.ui.button("Click").click([
  europe.build(page.data.plotly.choropleth(records, 'countries', 'size'))
])

page.ui.grid([
  [na],
  [europe, asia],
  [africa, sa],
])


