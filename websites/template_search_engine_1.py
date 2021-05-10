
import epyk as pk
import __init__
from ressources import fintech_analytics


page = pk.Page()
__init__.add_banner(page, __file__)
page.body.style.globals.font.size = 16
page.ui.contents().style.css.hide()
page.body.style.css.padding = "0 50px"
text1 = page.ui.texts.button("Mails")
text2 = page.ui.texts.button("Images")
page.ui.div([text1, text2], align="right")
page.ui.img("https://github.com/epykure/epyk-ui/blob/master/epyk/static/images/epyklogo_whole_big.png?raw=true",
            width=200, align="center")
page.ui.rich.search_input("Best Python web library")
page.ui.rich.search_results(fintech_analytics.ECOSYSTEM)

__init__.add_powered(page)
