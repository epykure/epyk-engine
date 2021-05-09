
import epyk as pk


# Test module to get test data
from epyk.tests import mocks


page = pk.Page()
page.headers.dev()

# https://codepen.io/sgratzl/pen/JxQVaZ?editors=0010


c = page.ui.charts.chartJs.custom(
  mocks.languages, y_columns=["rating", 'change'], x_axis='name',
  options={"type": 'boxplot', 'npm': 'chartjs-chart-box-and-violin-plot',
           'npm_path': r'C:\Angular\test-app\node_modules', 'script': 'Chart.BoxPlot'}
)

