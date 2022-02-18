
import epyk as pk
from epyk.mocks import urls as data_urls


# Create a basic report object
page = pk.Page()

h = page.ui.texts.highlights('''
This illustrates how to add bespoke JavaScript event to components.
All standard events are mapped and available.
''', icon="fab fa-js", type="info", options={"close": False})
h.style.css.background = "#f0db4f"

data_rest_1 = page.py.requests.csv(data_urls.DC_QUAKES)

# http://bl.ocks.org/d3noob/6077996
#data_rest_2 = page.py.requests.csv(data_urls.AIRPORT_TRAFFIC, store_location=r"C:\tmps")

# Main cross filter object
crossfilter = page.js.data.crossfilter(data_rest_1, "test")
dimension = crossfilter.dimension([('phases', str), ('magnitude', int)], 'test_dim')

# Sub dimension
d2 = page.js.data.crossfilter(cross_dimension=dimension.filterOnColumn("15", 'phases'), js_code="test_2")
dimension2 = d2.dimension([('agency', str), ('magnitude', int)], 'test_dim_2')
group = dimension2.group('group_name') # groupFunction('test_3', 'function(total) { return total[0] }')


d3 = page.js.data.crossfilter(cross_dimension=dimension.filterOnColumn("24", 'phases'), js_code="test_3")
dimension3 = d3.dimension([('agency', str), ('magnitude', int)], 'test_dim_3')
group3 = dimension3.GroupAll('group_name_3') # groupFunction('test_3', 'function(total) { return total[0] }')

c = page.ui.rich.console()

page.body.onReady([
  crossfilter, dimension, d2, dimension2, group,
  d3, dimension3, group3,

  c.dom.write(group.reduceSum('magnitude').all(), stringify=True),
  c.dom.write(dimension3.top(), stringify=True),
])

