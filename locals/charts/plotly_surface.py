
import epyk as pk


# Test module to get test data
from epyk.tests import mocks


page = pk.Page()
page.headers.dev()

data_series = mocks.getSeries(5, 30)

sur = page.ui.charts.plotly.surface(data_series, y_columns=[1], x_axis='x', z_axis=2)
