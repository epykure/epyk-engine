
import epyk as pk
import __init__

page = pk.Page()
__init__.add_banner(page, __file__)

page.body.style.globals.font.size = 20

site_reference = page.ui.texts.paragraph(
  "Using: &nbsp;", width="auto", options={"markdown": True})
site_reference.style.css.display = "inline-block"
site_reference.style.css.margin_top = 0
site_reference.style.css.margin_bottom = 0
banner = page.ui.banners.top("")

page.ui.contents().style.css.hide()

page.body.style.css.background = page.theme.greys[2]

img = page.ui.img("https://github.com/epykure/epyk-ui/blob/master/epyk/static/images/epyklogo_whole_big.png?raw=true", width=(300, 'px'))
img.style.effects.animate(
  "Test", {"filter": "blur(2px) grayscale(100%)"}, {"filter": "blur(0px) grayscale(0%)"}, duration=5)

title = page.ui.title("404 Error.", align="center")
title.style.css.font_size = 30

text = page.ui.text("We can't find the page you're looking for.", align="center")
button = page.ui.buttons.colored("Back to home", align="center")
button.style.css.margin_top = 10

div = page.ui.layouts.centered([img, title, text, button], align="center")
div.style.css.padding = "5% 10%"
div.style.css.margin_top = 80
div.style.configs.shadow()
div.style.css.background = page.theme.greys[0]

INFOS = '''
This will demonstrate how to:
- Build a page
- Change the theme 
- Set CSS Style to components
'''

powered = page.ui.rich.powered()
powered.style.css.display = "inline-block"
powered.style.css.width = "auto"
banner.extend([site_reference, powered])


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()
