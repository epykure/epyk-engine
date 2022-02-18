
import epyk as pk


# Create a basic report object
page = pk.Page()
page.headers.dev()

tb1 = page.ui.layouts.table()
tb1.style.css.border_collapse = "separate"
tb1.style.css.border_spacing = 10

# Add a header (first row is by default the header)
tb1 += [1, 2, 3]

# Change the CSS style of a cell in the header
tb1.get_header()[1].style.color = 'red'
tb1.get_header()[1].style.background = 'grey'

# Change all header cells style
for c in tb1.get_header():
  # This will add CSS attribute to the CSS inline section
  c.style.padding = 5
  c.style.border = "1px solid black"

# Create bespoke HTML component to be added to the table
span1 = page.ui.texts.span("Text 1").tooltip("Click to hide header last line")
span2 = page.ui.texts.span("Text 2")
span3 = page.ui.texts.span("Text 3").tooltip("Click to change table values")

# Add the row to the table (to the body)
tb1 += [span1, span2, span3]

span3.click([
  page.js.log(span3.dom.content),
  span2.build("New text"),

  # Change the cell properties
  #tb1[1].cell(1).dom.css({"background": page.theme.warning[0]})
  tb1[0][1].dom.css({"background": page.theme.warning[0]}),

  # Change the component in the cell
  tb1[0][1].val[0].dom.css({'text-decoration': 'underline'}),
])

# Add an extra row to the header
tb1.header += [4, 5]
tb1.get_header(1)[1].colspan(2)
tb1.get_header(1)[1].style.border = "1px solid black"

span1.click([
  # The display value must be table-row for a row
  tb1.get_header(1).dom.toggle()
])

# Add a text caption to this table
text = tb1.add_caption("This is a text attached to the table")
text.style.css.text_align = 'left'

# CSS class
# Create a bespoke CSS class for this report
from epyk.core.css.styles.classes import CssStyle

class MyCssBody(CssStyle.Style):
  _attrs = {'background': 'inherit'}
  _hover = {'background': page.theme.success[0]}

  _selectors = {'child': 'tbody td'}

# Attach the class to the component
tb1.style.add_classes.custom(MyCssBody)

# delete row
page.ui.button("Remove").click([
  tb1[0].dom.remove()
])
