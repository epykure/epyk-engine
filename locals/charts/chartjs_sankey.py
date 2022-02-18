
import epyk as pk


# Test module to get test data
from epyk.mocks import randoms


page = pk.Page()
page.headers.dev()

c = page.ui.charts.chartJs.custom(randoms.languages, y_columns=["rating", 'change'], x_axis='name',
                                    options={"type": 'sankey', 'npm': 'chartjs-chart-sankey',
                                             'npm_path': r'C:\Angular\node_modules'})


