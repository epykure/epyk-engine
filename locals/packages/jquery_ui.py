
import epyk as pk

from epyk.core.html import Html


class MyBody(Html.Body):
  def set_content(self, report, page_content):
    left = report.ui.div()
    but = report.ui.button("Click")
    but.click([
      report.js.alert("Test")
    ])
    left += but
    left.style.css.color = "white"
    right = report.ui.div("right")
    center = report.ui.div(page_content)
    div = report.ui.row([left, center, right])
    div[0].attr["class"].add("col-1")
    div[0].style.css.background_color = "grey"
    div[2].attr["class"].add("col-1")
    text = report.ui.text("text")
    text.options.managed = False
    div.options.managed = False
    self._html_content = "%s%s" % (div.html(), text.html())
    return self


# Create a basic report object
page = pk.Page()
page.headers.dev()

page.body = MyBody

p = page.ui.sliders.progressbar(30)
page.ui.date()
t = page.ui.fields.today()
#t.selectable(["2019-09-01", "2019-09-06"])
ti = page.ui.fields.now()
# s = page.ui.slider(recordSet=[1, 2, 3, 4, 5, 6, 7])

b = page.ui.button("Get")

b.click([
#  page.js.alert(s.dom.inViewPort),
  #page.js.alert(page.js.viewHeight),
  #page.js.alert(t.dom.content),
  #page.js.alert(p.dom.content),
  #page.js.alert(s.dom.content),
  #page.js.alert(ti.input.dom.content),
])

