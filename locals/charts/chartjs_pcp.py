
import epyk as pk


# Test module to get test data
from epyk.mocks import randoms


page = pk.Page()
page.headers.dev()

c = page.ui.charts.chartJs.custom(randoms.languages, y_columns=["rating", 'change'], x_axis='name',
                                    options={"type": 'pcp', 'npm': 'chartjs-chart-pcp',
                                             'script': 'Chart.PCP',
                                             'npm_path': r'C:\Angular\test-app\node_modules'})


