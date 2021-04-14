
import epyk as pk
from ressources import dating_data


page = pk.Page()
page.themes.red()
page.ui.contents().style.css.hide()
page.headers.title(dating_data.TITLE)

qrcode = page.ui.qrcode(dating_data.QRCODE)
qrcode.style.css.fixed(bottom=60, left=60)
qrcode.style.css.cursor = "pointer"
qrcode.style.css.z_index = 300

heart = page.ui.icon("fas fa-heart")
heart.style.css.color = page.theme.colors[-1]
heart.style.css.font_size = 20
heart.style.css.margin_left = 10
heart.style.css.margin_top = -20
heart.style.css.transform = "rotate(20deg)"

company = page.ui.text("Epyk")
company.style.css.color = page.theme.colors[-1]
company.style.css.font_size = "17px"
company.style.css.font_weight = 800
company.style.css.text_transform = 'uppercase'
company.style.css.letter_spacing = '2px'

navbar = page.ui.navbar(logo=page.ui.div([heart, company]), height=(100, 'px'), options={"status": False})
navbar.no_background()
navbar.style.padding = "30px"

# https://tinder.com/static/build/f92140b8942048e4fab4906b48c51db4.webp
bg = page.ui.images.wallpaper(dating_data.WALLPAPER)
bg.style.css.color = "white"
bg.add(page.ui.texts.absolute(dating_data.SLOGAN, size_notch=50))
bg.add(page.ui.texts.absolute(dating_data.SLOGAN_TEXT, align="center", size_notch=5, top=(60, "%")))

button = page.ui.button(dating_data.BUTTON_SIGN_UP)
button.style.no_class()
button.style.css.border_radius = "20px"
button.style.css.padding_top = "10px"
button.style.css.padding_bottom = "10px"
button.style.css.width = "20%"
button.style.css.color = "white"
button.style.css.cursor = "pointer"
button.style.css.absolute(top=(80, "%"), left=(50, "%"))
button.style.css.background = page.theme.colors[-1]
button.style.css.border_color = page.theme.colors[-1]
button.style.hover({"background": page.theme.notch(), "border-color": page.theme.notch(), "color": "white"})

bg.add(button)
