
import epyk as pk
import __init__


page = pk.Page()
__init__.add_banner(page, __file__)
page.ui.banners.corner("Webtemplate", position="top")
page.ui.contents().style.css.hide()

side = page.ui.navigation.side()
__init__.add_powered(page)