
import epyk as pk


# Test module to get test data
from epyk.mocks import randoms


page = pk.Page()
page.headers.dev()

data_series = randoms.getSeries(5, 30)

sur = page.ui.charts.plotly.surface(data_series, y_columns=[1], x_axis='x', z_axis=2)
