
import epyk as pk


page = pk.Page()
page.ui.banners.corner("Webtemplate", position="top")
page.ui.contents().style.css.hide()

side = page.ui.navigation.side()