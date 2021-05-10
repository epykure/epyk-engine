# https://www.fitbit.com/us/home

# TODO
# - add sliding effects
# - add vignet picture right
# - add footer

import epyk as pk
import __init__

page = pk.Page()
__init__.add_banner(page, __file__)

page.headers.favicon("https://www.fitbit.com/favicon.ico")
page.headers.title("Epyk (Fitbit)")
# <img src="/content/dam/fitbit/logo/FITBIT%20LOGO%20FOR%20HEADER.svg" alt="">

nav = page.ui.navbar(logo="https://www.fitbit.com/content/dam/fitbit/logo/FITBIT%20LOGO%20FOR%20HEADER.svg")
nav.no_background()

img_link = "https://www.fitbit.com/content/dam/fitbit/global/marketing-pages/home/tablet/4thofjuly-hero-tablet.jpg/jcr:content/renditions/4thofjuly-hero-tablet-1x.jpg"

text = page.ui.banners.text(" We believe Black lives matter. Learn how Fitbit is stepping up to support the movement both within our company and our communities.", background="rgb(0, 31, 63)")
text.style.css.color = "white"

main_banner = page.ui.images.background(img_link, height=(600, "px"))
text = page.ui.text("Everyone's goals have a place in the sun", width=(340, "px"), height=(600, "px"))
text.style.css.font_size = "60px"
text.style.css.display = "table-cell"
text.style.css.padding_left = "20px"
text.style.css.vertical_align = "middle"
text.style.css.color = "white"
main_banner.add(text)

ceo = page.ui.banners.text("Fitbit stands with the Black community", size_notch=40, background="black")
ceo.style.css.color = "white"

header = page.ui.banners.title("At Fitbit, health & fitness come first",
                               "Each Fitbit product includes these core features and more to inspire you on your journey.")

use1 = page.ui.images.background("https://www.fitbit.com/content/dam/fitbit/global/marketing-pages/home/static/activity-exercise-tracking.jpg/_jcr_content/renditions/original", align="left", position="bottom")
text = page.ui.text("Health & fitness app", width=(100, "%"))
text.style.css.position = "absolute"
text.style.css.bottom = 0
text.style.css.background = "rgba(0, 0, 0, 0.3)"
text.style.css.font_size = "26px"

text.style.css.color = "white"

use1.add(text)

use2 = page.ui.images.background("https://www.fitbit.com/content/dam/fitbit/global/marketing-pages/home/static/health-and-fitness.jpg/_jcr_content/renditions/original")
use3 = page.ui.images.background("https://www.fitbit.com/content/dam/fitbit/global/marketing-pages/home/static/innovative-sleep-tools.jpg/_jcr_content/renditions/original")

page.ui.row([use1, use2, use3])

page.ui.layouts.new_line()

url = "https://www.fitbit.com/content/dam/fitbit/global/marketing-pages/quiz/desktop/home-quiz-image-background.jpg/_jcr_content/renditions/original"

img = page.ui.vignets.image("Not sure which product is right for you?", "", image=url, width=(100, "%"))
img.style.css.background_color = "#E3E8F0"

disclaimer = page.ui.banners.text('''
*Only on devices with heart rate.
<br/>
**Some sleep features in the Fitbit app are only available when tracking via a device with heart rate.
''', align="left")
disclaimer.style.css.background_color = "#c3c8c9"

__init__.add_powered(page)
