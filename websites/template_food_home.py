from epyk.core.Page import Report
from ressources import fintech_analytics


page = Report()
page.ui.contents().style.css.hide()

page.headers.title(fintech_analytics.BANNER_TEXT)

navbar = page.ui.navbar(height=(100, 'px'))
navbar.logo.style.css.width = "80px"
navbar.logo.style.css.height = "80px"
navbar.style.css.border_bottom = None

row = [page.ui.images.background(url=picture["image"]) for picture in fintech_analytics.VIGNETS]
section = page.ui.titles.head(fintech_analytics.BUTTON_TWITTER, align="center")
section.style.css.color = "black"
section.style.css.margin_bottom = 20
menu = page.ui.col([section, page.ui.row(row)])
tabs = page.ui.panels.tabs()
for name in fintech_analytics.ITEMS:
  tabs.add_panel(
    name, menu if name == fintech_analytics.MENU_ITEMS_SELECTED else page.ui.div(),
    selected=name == fintech_analytics.MENU_ITEMS_SELECTED)

