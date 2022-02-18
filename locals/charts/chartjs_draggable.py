
import epyk as pk


# Test module to get test data
from epyk.mocks import randoms


# Create a basic report object
page = pk.Page()
page.headers.dev()


a = page.ui.charts.chartJs.line(randoms.languages, y_columns=["rating", 'change'], x_axis='name')
a.dragData()


box = page.ui.div()
box.style.css.background = "white"
box.style.css.padding_left = 10
box.style.css.padding_right = 10
box.extend([a])
box.style.configs.doc()
