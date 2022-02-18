
from epyk.core.Page import Report
from epyk.core.js import libs


page = Report()
page.headers.dev()
page.imports.google_products(['captcha'])

fr = page.ui.geo.jqv.france()
fr.options.multiSelectRegion = True
fr.click([
  page.js.console.log(libs.jqvmap.region),
  page.js.console.log(libs.jqvmap.code),
  page.js.console.log(libs.jqvmap.element),
  page.js.console.log("data", skip_data_convert=True),
])

page.ui.geo.jqv.europe()

cam = page.ui.media.camera()
page.ui.button("start").click([cam.dom.start()])
page.ui.button("play").click([cam.dom.play()])
page.ui.button("Stop").click([cam.dom.stop()])
page.ui.button("record (Start)").click([cam.dom.record()])
page.ui.button("record (Stop)").click([cam.dom.record(False)])
page.ui.button("takepicture").click([cam.dom.takepicture()])

page.ui.captcha()