
import epyk as pk

page = pk.Page()

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

title = page.ui.texts.absolute("Epyk Studio", size_notch=52, top=(30, "%"), left=(50, "%"))
title.style.css.white_space = "nowrap"
title.style.css.color = "white"
title.style.css.font_family = "Cursive"

# Add the content
title = page.ui.texts.absolute("coming soon", size_notch=52, top=(50, "%"), left=(50, "%"))
title.style.css.white_space = "nowrap"
title.style.css.color = "white"

time = page.ui.rich.countdown(day=1, month=5, year=2021, hour=0, minute=0, second=0)
title.style.css.text_weight = 5000
time.style.css.color = "white"
time.style.css.font_factor(10)
time.style.css.absolute(top=(60, "%"), left=(50, "%"))

#
hr = page.ui.layouts.hr(width=(40, "%"))
hr.style.css.margin = "auto"
hr.style.css.absolute(top=(55, "%"), left=(50, "%"))

bg.add(title)
bg.add(hr)
bg.add(time)
bg.style.color = "white"

content = page.ui.texts.absolute(
  "An excellent web Framework for Python", size_notch=12, bottom=(20, "px"), left=(10, "px"))
content.style.css.transform = ""
content.style.css.gradient_text("#3776ab", "#f0db4f", "right")
bg.add(content)

INFOS = '''
This will demonstrate how to:
- Build a page
- Change the page logo
- Add wallpaper
- Use a countdown component
'''

powered = page.ui.rich.powered()
powered.style.css.display = "inline-block"
powered.style.css.width = "auto"
banner.extend([site_reference, powered])


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()
