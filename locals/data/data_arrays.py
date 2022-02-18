
import epyk as pk


# Create a basic report object
page = pk.Page()

h = page.ui.texts.highlights('''
This illustrates how to add bespoke JavaScript event to components.
All standard events are mapped and available.
''', icon="fab fa-js", type="info", options={"close": False})
h.style.css.background = "#f0db4f"

# Console component
c = page.ui.rich.console(
  "* This is a log section for all the events in the different buttons *", options={"timestamp": True})

array = [1, 2, 3, 4, 5, 6]

page.body.onReady([
  # This does not require a Javascript Name as the object will be just converted and used as is
  c.dom.write(page.js.objects.list([1, 2, 3, 4, 5, 6]), stringify=True),

  # Create a non attached List and attached it to the report object before using the without feature
  c.dom.write(page.js.objects.list(array, page=page).without([3, 4]), stringify=True),

  # Transform a report object list and use underscore features
  # This will require a variable name as it will be stored on the javascript side
  c.dom.write(page.data.js.list("test", array).sample(3).first(1), stringify=True),

# Transform a report object list and use underscore features
  # This will require a variable name as it will be stored on the javascript side
  c.dom.write(page.data.js.list("test3", array).some.includes([3, 4]), stringify=True),

  # Transform a report object list and use underscore features
  # This will require a variable name as it will be stored on the javascript side
  c.dom.write(page.data.js.list("test2", [1, 2, 3, 4, 5, 6]).sample(3).rest(1), stringify=True),
])

