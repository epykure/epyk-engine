##

from epyk.core.Page import Report

from epyk.tests import data_urls


# Create a basic report object
page = Report()
page.headers.dev()

# retrieve some random json data
data_rest = page.py.requests.csv(data_urls.BLOG_OBJECT)

# create a json viewer object
j = page.ui.json(data_rest, height=(100, 'px'))

# change the default options
j.options.open = False
j.options.hoverPreviewEnabled = True

# add a button for interactivity
page.ui.button("Click").click([
  j.js.openAtDepth(0),
  j.build({"test": 'ok'})
])

