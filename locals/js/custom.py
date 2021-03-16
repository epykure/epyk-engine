
from epyk.core.Page import Report
from epyk.core.css.themes import ThemeBlue

# Create a basic report object
page = Report()
page.headers.dev()
page.theme = ThemeBlue.BlueGrey()
page.body.add_template(defined_style="doc")


page.ui.title("Custom / External JavaScript")

h = page.ui.texts.highlights(
  "This illustrates how to load external JavaScript modules and string and how to display results in the Browser console.",
  icon="fab fa-js", type="info", options={"close": False})
h.style.css.background = "#f0db4f"

# Add the file from the local environment context defined in Imports.STATIC_PATH
# This path will be overridden and specific to your configuration
page.js.customFile("test.js")

# https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.0.0/core.min.js
page.js.customFile("crypto-js.min.js", path='https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.0.0')

# Add a bespoke Javascript fragment at the beginning of the report
page.js.customText("console.log('The devil is in the detail')")

# Or this example use a function from the module crypto.
# More details about the Javascript library here: https://github.com/brix/crypto-js
page.js.customText("console.log(CryptoJS.SHA256('Message'))")

# Even if it is not recommended it is also possible to define Javascript functions
page.js.customText("function myJsFnc(data){ return data + 10}")

p = page.ui.texts.paragraph('''
It is important to use Epyk's interfaces just for a glue to JavaScript components and to push
to the external module for changes.
It is important to share and be collaborative in Open Source libraries.
''')
p.style.css.border = "1px dashed black"
p.style.css.background = "#EBF0E2"
p.style.css.padding = 5

# And to use it in any Javascript event
button = page.ui.button("Click").click([
  # Skip the conversion to not consider it as a Python String
  page.js.console.log("myJsFnc(5)", skip_data_convert=True),

  # It is also possible to add this fragment directly in the function by using Javascript objects primitives
  # In this example the function is anonymous
  page.js.console.log(page.js.objects.get("(function(data){return data + 20})(5)"))
])
button.style.css.background = "#323330"
button.style.css.color = "#f0db4f"
button.style.css.border_color = "#323330"

page.ui.layouts.hr()
page.ui.titles.subtitle("Report powered by")
page.ui.rich.powered()

if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()


