
import epyk as pk
from epyk.core import data

from epyk.mocks import randoms


# Create a basic report object
page = pk.Page()
page.headers.dev()

#
result = data.plotly.surface(randoms.languages, y_columns=['rating'], x_axis="change", z_axis="change")

nvd3 = data.c3.y(randoms.languages, y_columns=['change'], x_axis="name")

#print(result)
# print(data_rest)