
import epyk as pk
import pandas as pd
from epyk.tests import data_urls

page = pk.Page()
# CSS Style
page.body.style.css.padding = 10
# Retrieve data
records = pd.DataFrame(page.py.requests.csv(data_urls.DEMO_COUNTRY))
records = records[records["Year"] == "2010"]
# Create a link to download data as a Json file
viewer = page.ui.json(records.to_dict())
viewer.options.hoverPreviewEnabled = True
viewer.options.hoverPreviewArrayCount = 5
# Transpile to HTML file
page.outs.html_file(name="outJson")
