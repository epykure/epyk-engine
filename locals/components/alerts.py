
from epyk.core.Page import Report
from epyk.core.css.themes import ThemeBlue


# Create a basic report object
page = Report()
page.headers.dev()
page.verbose = True # Display the system logs
page.theme = ThemeBlue.BlueGrey()
page.body.add_template(defined_style="doc")

# Create an input text field.
input = page.ui.input(placeholder="Write your text and press show")
number = page.ui.input(placeholder="Write a number and press show (Xs)")

# Define the popup object.
danger = page.ui.network.warning()
danger.options.time = None
danger.options.close = False

# Button to display the popup.
button1 = page.ui.button("Show")
button1.click([
  danger.build(input.dom.content)
])

# Button to display the popup with a timer.
button2 = page.ui.button("Show (Xs)")
danger.options.config_js({"time": number.dom.content})
print("ok")
button2.click([
  danger.build(input.dom.content, {"time": number.dom.content})
])
print("done")
