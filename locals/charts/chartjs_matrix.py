
import epyk as pk


# Test module to get test data
from epyk.tests import mocks


page = pk.Page()
page.headers.dev()


c = page.ui.charts.chartJs.custom(mocks.languages, y_columns=["rating", 'change'], x_axis='name',
                                    options={"type": 'matrix', 'npm': 'chartjs-chart-matrix',
                                             'npm_path': r'C:\Angular\test-app\node_modules'})

c.plugins.zoom.zoom.enabled = True
c.plugins.zoom.zoom.mode = 'xy'
c.plugins.zoom.zoom.drag = True
c.plugins.zoom.pan.enabled = True
c.plugins.zoom.pan.mode = 'xy'

c.plugins.zoom.zoom.onZoom([
  page.js.console.log("Test")
])

