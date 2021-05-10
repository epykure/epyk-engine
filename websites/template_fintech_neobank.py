
import epyk as pk
import __init__

from ressources import fintech_analytics
from ressources import link_data

page = pk.Page()
__init__.add_banner(page, __file__)

page.themes.blue_light()
page.ui.contents().style.css.hide()
page.body.style.globals.size = 12

nav = page.ui.navbar(logo=page.ui.text("Epyk"), height=(60, "px"))
nav.style.css.position = "block"
page.body.add_template(defined_style="margins")
page.body.style.globals.size = 12

i = 0
v0 = page.ui.vignets.image(
  fintech_analytics.VIGNETS[i]['title'], content=fintech_analytics.VIGNETS[i]['content'],
  image=fintech_analytics.VIGNETS[i]['image'],
  height=(200, 'px'))

v1 = page.ui.vignets.price("XXX", "Open Source", fintech_analytics.ITEMS, currency="$")
v2 = page.ui.img(link_data.IMG_WORLD, path=link_data.IMG_STATIC_PATH)
row = page.ui.row([v1, [page.ui.title("Can be used everywhere", align="center"), v2]])
row.set_size_cols(3)

__init__.add_powered(page)