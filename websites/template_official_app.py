
import epyk as pk
from ressources import fintech_analytics
from ressources import link_data

page = pk.Page()
page.ui.contents().style.css.hide()

logo = page.ui.text("Epyk")
logo.style.css.color = "white"
logo.style.css.margin_left = 10

nav = page.ui.navbar(logo=logo, height=(40, 'px'))
nav.style.css.background = "#1ebea5"

for section in fintech_analytics.TITLES:
  nav.add(section)
  nav[-1].style.css.color = "white"
  nav[-1].style.css.font_size = "17px"
  nav[-1].style.css.font_weight = 500
  nav[-1].style.css.margin_left = '20px'
  nav[-1].style.css.text_overflow = "ellipsis"

text1 = page.ui.rich.adv_text(
  fintech_analytics.TEXT_ADV['section'], fintech_analytics.TEXT_ADV['title'], fintech_analytics.TEXT_ADV['content'],
  background="#faf7eb")
text2 = page.ui.rich.adv_text(
  fintech_analytics.TEXT_ADV_2['section'], fintech_analytics.TEXT_ADV_2['title'], fintech_analytics.TEXT_ADV_2['content'],
  background="#d0e9ea")

container = page.ui.div(height=(100, "%"))
div = page.ui.div(width=(100, "%"))

div.add(
  page.ui.images.carousel([
    fintech_analytics.WALLPAPER,
    fintech_analytics.WALLPAPER2,
  ]))
container.add(div)
container.style.css.text_align = "center"
container.style.css.background = "#faf7eb"

container2 = page.ui.div()
div2 = page.ui.div(height=(400, "px"), width=(300, "px"))
div2.style.css.background_url(link_data.BACKGROUND_2)
container2.style.css.background = "#d0e9ea"
container2.add(div2)
container2.style.css.text_align = "center"

row = page.ui.row([
  page.ui.col([text1, container], position="top", height=(100, "%")),
  page.ui.col([text2, container2], height=(100, "vh"))], height=(100, "vh"))
row.options.noGutters = True
