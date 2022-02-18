

from epyk.core.Page import Report
from epyk.mocks import urls as data_urls


# Create a basic report object
page = Report()
page.headers.dev()

# Add empty lines using HTML tag
page.ui.layouts.new_line(10)

# Add a popup with some HTML components
example = page.ui.title("Example")
text = page.ui.text("This is a text")
example.style.css.color = 'red'
data_rest = page.py.requests.csv(data_urls.PLOTLY_APPLE_PRICES)
ts = page.ui.charts.chartJs.timeseries(data_rest, y_columns=['AAPL.Open'], x_axis="Date")

# Create a postit anchor to display the popup when the mouse is on it.
p = page.ui.postit([example, text, ts])
p.anchor.style.css.margin_left = '50px'
p.popup.style.css.height = "250px"
p.popup.style.css.width = "300px"
