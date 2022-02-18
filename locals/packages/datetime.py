

import epyk as pk


page = pk.Page()

dt1 = page.ui.fields.date()
dt1.excluded_dates(["2021-05-01"])

dt1.input.options.appendText = "Test"
dt1.input.options.buttonText = "Run"

dt1.input.options.onClose([
  page.js.alert("Closing")
])

btn = page.ui.button("Click")
btn.click([
  dt1.input.js.disable()
])
