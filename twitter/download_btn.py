
import epyk as pk
import pandas as pd
from epyk.tests import data_urls

page = pk.Page()
# CSS Style
page.body.style.css.padding = 10
# Retrieve data
records = pd.DataFrame(page.py.requests.csv(data_urls.DEMO_COUNTRY))
# Create a link to download data as a Json file
btn = page.ui.links.data("Get data", records.to_json())
btn.style.css.border = "1px solid grey"
# Transpile to HTML file
page.outs.html_file(name="outDownload")
