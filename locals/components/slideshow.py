
from epyk.core.Page import Report

# Create a basic report object
page = Report()
page.headers.dev()


ss = page.ui.slideshow([page.ui.text("Great results %s" % i) for i in range(20)])

ss.add_index_changed([
  page.js.console.log("ok"),
  page.js.console.log(ss.dom.info.indexCached),
  page.js.console.log(ss.dom.info.index),
])

page.ui.button("test").click([
  #ss.js.first(),
  #page.js.console.log(ss.dom.getInfo()),
  ss.dom.info.set(),
  page.js.console.log(ss.dom.info.nextButton.innerHTML()),
  page.js.console.log(ss.dom.val)
])