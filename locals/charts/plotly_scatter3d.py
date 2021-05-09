
import epyk as pk


# Test module to get test data
from epyk.tests import data_urls


page = pk.Page()
page.headers.dev()

data = page.py.requests.csv(data_urls.PLOTLY_WEBGL_POLAR)


s3d = page.ui.charts.plotly.scatter3d(data, y_columns=["trial_1_theta", "trial_2_theta"], x_axis="trial_3_r", z_axis=["trial_1_r", "trial_2_r"])
s3d.data.opacity = 0.5
s3d.layout.grid_colors('white')
s3d.layout.axis_colors('white')
s3d.layout.no_background()

