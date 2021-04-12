
from epyk.core.Page import Report


page = Report()

page.body.style.globals.font.size = 20

site_reference = page.ui.texts.paragraph(
  "Inspired by [W3School](https://www.w3schools.com/howto/howto_css_coming_soon.asp) and using: &nbsp;",
  width="auto", options={"markdown": True})
site_reference.style.css.display = "inline-block"
site_reference.style.css.margin_top = 0
site_reference.style.css.margin_bottom = 0
banner = page.ui.banners.top("")

page.ui.contents().style.css.hide()

img = page.ui.img("https://github.com/epykure/epyk-ui/blob/master/epyk/static/images/epyklogo_whole_big.png?raw=true", width=(300, 'px'))
img.style.css.margin_top = "10%"

# Add the content
title = page.ui.texts.absolute("coming soon", size_notch=52, top=(70, "%"), left=(50, "%"))
title.style.css.white_space = "nowrap"

time = page.ui.texts.absolute("Work in progress", size_notch=12, top=(78, "%"), left=(50, "%"))
time.style.css.color = page.theme.greys[4]
time.style.css.italic()

title.style.css.text_weight = 5000

#
hr = page.ui.layouts.hr(width=(40, "%"))
hr.style.css.margin = "auto"
hr.style.css.absolute(top=(55, "%"), left=(50, "%"))

button = page.ui.buttons.colored("Back to home", align="center")
button.style.css.margin_top = 10

p = page.ui.sliders.progressbar()
p.style.css.margins(left=(20, "%"), right=(20, "%"))
p.style.css.position = "absolute"
p.style.css.bottom = "5%"

page.body.onReady([
  page.js.window.setInterval([
    p.build(page.js.math.random(1, 100))], "interval", milliseconds=1000)
])

powered = page.ui.rich.powered()
powered.style.css.display = "inline-block"
powered.style.css.width = "auto"
banner.extend([site_reference, powered])


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()
