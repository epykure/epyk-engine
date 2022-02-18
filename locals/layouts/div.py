
import epyk as pk

# Create a basic report object
page = pk.Page()
page.headers.dev()

# Create s simple container with Python code as String
div1 = page.ui.div("This is a text")

# Create a div container with two HTML components
t1 = page.ui.texts.span("This is a text 1")
t2 = page.ui.texts.span("This is a text 2")

# This is a container of components
div2 = page.ui.div([t1, t2])
for c in div2:
  # Change the style of the underlying components
  # The underlying components will be in the same row
  c.style.css.display = "inline-block"

# Change the style of the container
div2.style.css.border = "1px solid black"

# Change the CSS style of the container
div2.style.css.width = "auto"
div2.style.css.padding = 5
div2.style.css.display = "inline-block"

# Change the color of the text component after the builder
div2[1].onReady([
  # Change the CSS Style of the underlting component on ready
  div2[1].dom.css({"color": 'red'})
])

# Add even of an underlying component
div2[0].click([
  # The component w
  page.js.console.log("Add a log"),
  div2[1].build("New content"),

  # Select the content of the text container
  div2[1].dom.select()
])

page.ui.button("Load").click([
  page.js.console.log(div2.dom.content),
  # Empty the container
  div2.dom.empty(),

  # Load HTML in the container
  # add another internal component. The manage flag remove the component from the scope of the report
  div2.build(page.ui.tags.h1("This is a title", options={"managed": False}).css({"color": 'blue'}).html())
])

