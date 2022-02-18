from epyk.core.Page import Report

# Create a basic report object
page = Report()
page.headers.dev()

# Enable Google Maps
# By default all Google products are disabled
page.imports.google_products(['maps'])

# Use the Google map online library with the coordinates.
map = page.ui.geo.google.terrain(-33.92, 151.25)

# Click event to add interactivity on the page
page.ui.button("Click").click([
  map.js.setMapTypeId('satellite'),
  map.js.setHeading(45),
])

#page.ui.geo.google.current()
