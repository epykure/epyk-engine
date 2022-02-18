
from epyk.core.Page import Report

page = Report()
page.headers.dev()

page.verbose = True

path = page.ui.input(placeholder="Set your path here")

qrcode = page.ui.qrcode()

# Change the qrcode options
qrcode.options.colorDark = "orange"
qrcode.options.size = 50

path.enter([
  qrcode.build(path.dom.content)
])

button = page.ui.button("Google QRCode")
button.click([
  qrcode.js.makeCode("https://www.google.com/")
])

button = page.ui.button("Clear")
button.click([
  qrcode.js.clear()
])
