
import epyk as pk


# Test module to get test data
from epyk.mocks import randoms

# Create a basic report object
page = pk.Page()
page.headers.dev()


a = page.ui.charts.chartJs.line(randoms.languages, y_columns=["rating", 'change'], x_axis='name')
a.colors(["#FFFF00", "#FFA500"])

#a = page.ui.charts.apex.line(mocks.languages, y_columns=["rating", 'change'], x_axis='name')
#a.colors(["#FFFF00", "#FFA500"])

#a = page.ui.charts.c3.bar(mocks.languages, y_columns=["rating", 'change'], x_axis='name')
#a.colors(["#FFFF00", "#FFA500"])


#a = page.ui.charts.billboard.line(mocks.languages, y_columns=["rating", 'change'], x_axis='name')
#a.colors(["#FFFF00", "#FFA500"])

#a = page.ui.charts.nvd3.scatter(mocks.languages, y_columns=["rating", 'change'], x_axis='name')
#a.colors(["#FFFF00", "#FFA500"])

a = page.ui.charts.plotly.line(randoms.languages, y_columns=["rating", 'change'], x_axis='name')
a.colors(["#FFFF00", "#FFA500"])