
from epyk.core.Page import Report

from epyk.tests import data_urls
from epyk.tests import mocks


# Create a basic report object
page = Report()
page.headers.dev()

data_rest_1 = page.py.requests.json(data_urls.PIVOTTABLE_DATA)

# Create a table

tb1 = page.ui.tables.pivots.c3(mocks.languages, ['name'], ['type'])
tb1.renderers.c3.stacked()
