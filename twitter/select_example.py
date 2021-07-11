
import epyk as pk

page = pk.Page()
# Add a select box
selections = ["Tropical", "Dry", "Temperate", "Continental"]
select = page.ui.fields.select(
  pk.inputs.select.from_list(selections), label="Climates")
# Add a field input component with label and input
name = page.ui.fields.input(label="Add type: ")
name.input.enter([ # Add event to the input sub component
  select.input.js.add(name.dom.content, name.dom.content)
])
select.move() # Move the component after the input

page.outs.html_file(name="outSelect")
