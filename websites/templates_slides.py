import epyk as pk
from ressources import fintech_analytics

page = pk.Page()
page.body.style.globals.size = 18
slides = page.ui.vignets.slides(start=1)
page.ui.contents().style.css.hide()
slides.style.css.display = "block"

slides.add_slide("This is a title", [
  page.ui.title("Page 1")
])
slides[-1].style.css.background = 'white'

button_style = {"border-radius": '20px', 'background-color': 'rgb(0, 175, 245)', 'color': 'white', 'padding': '8px 25px', 'font-size': '18px'}
button = page.ui.button(fintech_analytics.BUTTON_TRY, align="center")
button.css(button_style)
button.style.css.margin_top = 10
text_vignet = page.ui.text(fintech_analytics.BANNER_TEXT, width=(100, "%"))
text_vignet.style.css.display = False

button.click([text_vignet.dom.show()])
content = page.ui.col([text_vignet, button])
content.style.css.padding = 0

for i, vignet in enumerate(fintech_analytics.VIGNETS):
  slides.add_slide("Title %s" % (i+1), [
    page.ui.vignets.image(vignet['title'], content=content, image=vignet['image'])
  ])

slides[-1].style.css.background = 'white'
slides[-1].style.css.background = 'white'
