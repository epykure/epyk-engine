
import epyk as pk
import __init__

page = pk.Page()
__init__.add_banner(page, __file__)

page.body.style.globals.font.size = 20

site_reference = page.ui.texts.paragraph(
  "Inspired by [W3School](https://www.w3schools.com/howto/howto_css_coming_soon.asp) and using: &nbsp;",
  width="auto", options={"markdown": True})
site_reference.style.css.display = "inline-block"
site_reference.style.css.margin_top = 0
site_reference.style.css.margin_bottom = 0

banner = page.ui.banners.top("")
banner.style.css.z_index = 2000
page.ui.contents().style.css.hide()

page.headers.favicon("https://raw.githubusercontent.com/epykure/epyk-ui/master/epyk/static/images/epyklogo.ico")
bg = page.ui.images.wallpaper("https://wallpapercave.com/wp/wp3188042.jpg")

# Add the company logo
logo = page.ui.images.logo("https://raw.githubusercontent.com/epykure/epyk-ui/master/epyk/static/images/epyklogo.ico")
logo.style.css.margin_top = 90
logo.style.css.transform = "scale(2.5)"

# Add the content
title = page.ui.texts.absolute("coming soon", size_notch=52, top=(50, "%"), left=(50, "%"))
title.style.css.white_space = "nowrap"
title.style.css.color = "white"

time = page.ui.texts.absolute("35 days left", size_notch=12, top=(60, "%"), left=(50, "%"))
title.style.css.text_weight = 5000
time.style.css.color = "white"

#
hr = page.ui.layouts.hr(width=(40, "%"))
hr.style.css.margin = "auto"
hr.style.css.absolute(top=(55, "%"), left=(50, "%"))

bg.add(title)
bg.add(hr)
bg.add(time)
bg.style.color = "white"

content = page.ui.texts.absolute(
  "An excellent web library for Python", size_notch=12, bottom=(20, "px"), left=(10, "px"))
content.style.css.transform = ""
content.style.css.background = "-webkit-linear-gradient(#3776ab, #f0db4f)"
content.css({"-webkit-text-fill-color": "transparent", "-webkit-background-clip": "text"})

bg.add(content)

INFOS = '''
This will demonstrate how to:
- Build a page
- Change the page logo
- Add wallpaper
'''

powered = page.ui.rich.powered()
powered.style.css.display = "inline-block"
powered.style.css.width = "auto"
banner.extend([site_reference, powered])


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()
