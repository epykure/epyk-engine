from epyk.core.Page import Report

# Import the internal mocks data for examples
from epyk.mocks import randoms


# Create a basic report object
page = Report()
page.headers.dev()

# Enable Google Tables
# By default all Google products are disabled
page.imports.google_products(['tables'])

# Create a basic table using google online library
# This cannot be installed locally.
page.ui.tables.google.table(randoms.languages, rows=["rating", 'change'])
