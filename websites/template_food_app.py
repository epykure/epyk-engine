import epyk as pk
import __init__
from ressources import fintech_analytics


page = pk.Page()
__init__.add_banner(page, __file__)
page.themes.pink(dark=False)

#skin = page.skins.fireworks()
#skin.style.css.position = "fixed"
#skin.style.css.left = 0

page.body.style.globals.font.size = 16
page.ui.contents().style.css.hide()
page.body.add_template(defined_style="margins")
page.headers.title(fintech_analytics.TITLE)

navbar = page.ui.navbar(title="Epyk", options={"status": False})
navbar.style.css.border_bottom = None
navbar.style.css.background = page.theme.notch()

bt = page.ui.icons.twitter(fintech_analytics.BUTTON_TWITTER, width="auto")
bt.style.css.margin_left = 5
t = page.ui.text(fintech_analytics.TEXT_OPENSOURCE).css({"margin-bottom": '10px'})
t.style.css.padding_left = 5
content = page.ui.div([])
content.add(t)
content.add(page.ui.layouts.new_line())
content.add(bt)

v = page.ui.vignets.image(title=fintech_analytics.BANNER_TEXT, width=(100, '%'), content=content, image=fintech_analytics.WALLPAPER)
v.style.css.background = page.theme.greys[2]
v.style.css.border = "1px solid %s" % page.theme.greys[5]
v.style.css.padding_top = 20
v.style.css.padding_bottom = 20
v.title.style.css.margin_left = 5

page.ui.banners.title(title=fintech_analytics.BANNER_TEXT, content=fintech_analytics.QUOTE)

row = []
for v in fintech_analytics.VIGNETS:
  image = page.ui.vignets.image(title=v["title"], render="col", image=v["image"], content=v["content"])
  image.style.css.border = "1px solid %s" % page.theme.greys[2]
  image.style.css.display = "inline-block"
  image.style.css.margin = 5
  image.style.css.padding_top = 10
  image.style.css.padding_bottom = 10
  image.style.css.width = "calc(50% - 30px)"
  row.append(image)

row_vignets = page.ui.div(row, align="center", position="top")
row_vignets.style.css.display = "inline-block"

page.ui.banners.title(title=fintech_analytics.BANNER_TEXT, content=fintech_analytics.QUOTE)

img = page.ui.img(fintech_analytics.GIF, width=(300, 'px'))
page.body.style.css.padding_bottom = 20

__init__.add_powered(page)

