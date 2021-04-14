
import epyk as pk


page = pk.Page()
page.ui.banners.corner("Webtemplate", position="top")
page.ui.contents().style.css.hide()
page.body.add_template(defined_style="margins")

t = page.ui.text("Test")
side = page.ui.navigation.side([t])


img = page.ui.img(
  "https://images.pexels.com/photos/267389/pexels-photo-267389.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500", width=(40, '%'))
img.style.css.display = "inline-block"
img2 = page.ui.img(
  "https://images.pexels.com/photos/2265482/pexels-photo-2265482.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500", width=(40, '%'))
img2.style.css.display = "inline-block"
img.style.css.margin_right = "5%"
img.style.css.margin_left = "5%"
img2.style.css.margin_right = "5%"

page.ui.panels.sliding([img, img2], title="My apps")

