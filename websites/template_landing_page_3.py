import epyk as pk
import __init__
from ressources import blablacar_data

page = pk.Page()
__init__.add_banner(page, __file__)
page.ui.contents().style.css.hide()

svg = page.ui.charts.svg.new((1199.96, 'px'), (1014.39, 'px'))
svg.style.css.width = 33
svg.style.css.height = 33
svg.path(fill="#054752", x=1195.16, y="619.8c-31.2-184-205.8-308-390-276.8l54.4-308.3L662.96 0c-17 37-91 206-127 397 73.3 50 127 128.5 143 223 17.2 100.7-12.3 198.5-72.6 271.7 14.8 18 31.7 34.7 51 49.7 77 60.3 170.2 83.8 261 68.4 184-31.3 308-206 276.8-390z")
svg.path(fill='#2dbeff', x=531.96, y="418l4-21c-69.8-47.6-157.2-69.3-247-54l54.4-308.4L146.66 0c-17.5 38.4-96.5 218.6-130.7 418-27.5 159.8-26.2 332 58.5 453 18.2 26 40.2 49.7 66.7 70.4 77 60.3 170.2 83.8 261 68.4 83.4-14 154.4-57.7 204.3-118.2-5.5-6.7-10.8-13.6-15.7-20.7-85-121.2-86-293.3-58.7-453z")
svg.path(fill="#9ef769", x=678.96, y="619.8c-16-94.4-69.7-173-143-223l-4 21c-27.4 160-26 332 58.6 453 5 7.2 10.2 14 15.7 20.8 60.3-73.2 89.8-171 72.7-271.8z")

page.ui.navbar(logo=svg, height=(60, "px"))

page.ui.banners.info(blablacar_data.COVID, background="#EDEDED")

bg = page.ui.images.background(url=blablacar_data.BACKGROUND_IMAGE, height=(500, "px"))
bg.add(page.ui.vignets.vignet(blablacar_data.VIGNET['title'], blablacar_data.VIGNET['content'], width=("auto", "")))
bg.style.css.color = "white"

button_style = {"border-radius": '20px', 'background-color': 'rgb(0, 175, 245)', 'color': 'white', 'padding': '8px 25px', 'font-size': '18px'}
button_inv_style = {"border-radius": '20px', 'background-color': 'white', 'color': 'rgb(0, 175, 245)', 'padding': '8px 25px', 'font-size': '18px'}
title_style = {"width": '90%', 'margin': 'auto', 'font-weight': 800, 'line-height': '1.06', 'font-size': '30px', 'color': 'rgb(5, 71, 82)', 'padding': '24px 0px'}

button = page.ui.button(blablacar_data.BUTTON_OFFER_RIDW, align="center")
button.style.css.margin_top = 10
button.css(button_style)

content = page.ui.col([page.ui.text(blablacar_data.SLOGAN, width=(100, "%")), button])
content.style.css.padding = 0

page.ui.vignets.image(blablacar_data.VIGNET_2['title'], content=content, image=blablacar_data.VIGNET_2['image'])
page.ui.titles.title(blablacar_data.TITLE_1).css(title_style)

row = []
for k, v in blablacar_data.CATEGORIES.items():
  row.append(page.ui.vignets.vignet(title=k, content=v))
page.ui.row(row, align="center", position="top")
page.ui.titles.title(blablacar_data.TITLE_2).css(title_style)

svg = page.ui.charts.svg.new((24, 'px'), (24, 'px'))
svg.style.css.width = 80
svg.style.css.height = 80
svg.path(fill="#708C91", x="19.33,8.5c0-0.276-0.225-0.5-0.5-0.5h-3.855c-0.275,0-0.5,0.224-0.5,0.5s0.225,0.5,0.5,0.5h3.855 C19.105,9,19.33,8.776,19.33,8.5z", y="")
svg.path(fill="#708C91", x="9.906,8.492V8.133c0-0.994-0.798-1.799-1.781-1.799S6.344,7.139,6.344,8.133v0.359 c0,0.994,0.798,1.799,1.781,1.799S9.906,9.486,9.906,8.492z", y="")
svg.path(fill="#708C91", x="4.167,13.422v0.528c0,0.165,0.134,0.3,0.3,0.3h7.316c0.166,0,0.3-0.135,0.3-0.3v-0.528 c0-0.713-0.474-1.339-1.162-1.526c-0.75-0.204-1.773-0.417-2.797-0.417s-2.047,0.213-2.797,0.417 C4.641,12.083,4.167,12.709,4.167,13.422z", y="")
svg.path(fill="#708C91", x="12,18H1.982V1h2.904C5.11,2.139,6.086,3,7.265,3c1.178,0,2.154-0.861,2.379-2h4.88 c0.225,1.139,1.201,2,2.379,2s2.154-0.861,2.379-2h2.903v9c0,0.276,0.224,0.5,0.5,0.5s0.5-0.224,0.5-0.5V0.5 c0-0.276-0.224-0.5-0.5-0.5H18.83c-0.276,0-0.5,0.224-0.5,0.5c0,0.833-0.643,1.5-1.428,1.5s-1.428-0.667-1.428-1.5 c0-0.276-0.224-0.5-0.5-0.5H9.192c-0.276,0-0.5,0.224-0.5,0.5c0,0.833-0.643,1.5-1.427,1.5S5.837,1.333,5.837,0.5 c0-0.276-0.224-0.5-0.5-0.5H1.482c-0.276,0-0.5,0.224-0.5,0.5v18c0,0.276,0.224,0.5,0.5,0.5H12c0.276,0,0.5-0.224,0.5-0.5 S12.276,18,12,18z", y="")
svg.path(fill="#708C91", x="25.354,13.646c-0.195-0.195-0.512-0.195-0.707,0L19,19.293l-2.646-2.646c-0.195-0.195-0.512-0.195-0.707,0 s-0.195,0.512,0,0.707l3,3c0.195,0.195,0.512,0.195,0.707,0l6-6C25.549,14.158,25.549,13.842,25.354,13.646z", y="")

v1 = page.ui.vignets.vignet(title=blablacar_data.VIGNET_3['title'], icon=svg, content=blablacar_data.VIGNET_3['content'])
svg = page.ui.charts.svg.new((24, 'px'), (24, 'px'))
svg.style.css.width = 80
svg.style.css.height = 80
svg.path(fill="#054752", x="22.9,8.2l-3-4C19.807,4.074,19.657,4,19.5,4H15V1.5C15,1.224,14.775,1,14.5,1h-6C8.224,1,8,1.224,8,1.5V4H2.5 C2.224,4,2,4.224,2,4.5v8C2,12.775,2.224,13,2.5,13H8v10.5C8,23.775,8.224,24,8.5,24h6c0.275,0,0.5-0.225,0.5-0.5V13h4.5 c0.157,0,0.307-0.074,0.4-0.2l3-4C23.033,8.622,23.033,8.378,22.9,8.2z M9,2h5v2H9V2z M14,23H9V13h5V23z M19.25,12H3V5h16.25 l2.625,3.5L19.25,12z", y="")
v2 = page.ui.vignets.vignet(title=blablacar_data.VIGNET_4['title'], icon=svg, content=blablacar_data.VIGNET_4['content'])

svg = page.ui.charts.svg.new((24, 'px'), (24, 'px'))
svg.style.css.width = 80
svg.style.css.height = 80
svg.path(fill="#054752", x="9,23.5c-0.133,0-0.261-0.053-0.355-0.147C8.312,23.017,0.5,15.085,0.5,10c0-5.321,4.322-8.5,8.5-8.5 c4.178,0,8.5,3.179,8.5,8.5c0,1.083-0.353,2.37-1.049,3.825c-0.119,0.249-0.419,0.354-0.667,0.235 c-0.249-0.119-0.354-0.418-0.235-0.667C16.18,12.074,16.5,10.932,16.5,10c0-4.695-3.813-7.5-7.5-7.5S1.5,5.305,1.5,10 c0,4.098,5.967,10.661,7.5,12.279c0.462-0.487,1.327-1.424,2.303-2.599c0.177-0.213,0.492-0.241,0.704-0.065 c0.212,0.177,0.242,0.492,0.065,0.704c-1.475,1.776-2.667,2.982-2.718,3.032C9.261,23.446,9.133,23.5,9,23.5z", y="")
svg.path(fill="#054752", x="9,13.5c-1.93,0-3.5-1.57-3.5-3.5S7.07,6.5,9,6.5s3.5,1.57,3.5,3.5S10.93,13.5,9,13.5z M9,7.5 c-1.378,0-2.5,1.122-2.5,2.5s1.122,2.5,2.5,2.5s2.5-1.122,2.5-2.5S10.378,7.5,9,7.5z", y="")
svg.path(fill="#054752", x="20,20.5c-0.128,0-0.256-0.049-0.354-0.146c-0.195-0.195-0.195-0.512,0-0.707l2.146-2.146H14 c-0.276,0-0.5-0.224-0.5-0.5s0.224-0.5,0.5-0.5h7.793l-2.146-2.146c-0.195-0.195-0.195-0.512,0-0.707s0.512-0.195,0.707,0 l2.999,2.999c0.004,0.004,0.008,0.008,0.011,0.012l0,0c0.001,0,0.001,0,0.001,0c0,0.001,0.001,0.001,0.001,0.001l0,0 c0.042,0.046,0.075,0.097,0.097,0.151c0.022,0.055,0.036,0.113,0.038,0.176l0,0c0,0,0,0,0,0.001c0,0,0,0,0,0.001l0,0 c0,0.009,0,0.017,0,0.025l0,0c0,0.001,0,0.001,0,0.001c0,0.001,0,0.001,0,0.001l0,0c-0.002,0.062-0.016,0.121-0.038,0.176 c-0.021,0.055-0.055,0.105-0.097,0.151l0,0c0,0-0.001,0-0.001,0.001c0,0,0,0-0.001,0l0,0c-0.003,0.004-0.007,0.008-0.011,0.012 l-2.999,2.999C20.256,20.451,20.128,20.5,20,20.5z", y="")

v3 = page.ui.vignets.vignet(title=blablacar_data.VIGNET_5['title'], icon=svg, content=blablacar_data.VIGNET_5['content'])
page.ui.row([v1, v2, v3], align="center", position="top")

button = page.ui.button(blablacar_data.BUTTON_DISCOVER, align="center")
button.css(button_style)
button.style.css.margin_top = 10
content = page.ui.col([page.ui.text(blablacar_data.TEXT_DISCOVERY, width=(100, "%")), button])
content.style.css.padding = 0
page.ui.vignets.image(blablacar_data.VIGNET_6['title'], content=content, image=blablacar_data.VIGNET_6['image'])

page.ui.banners.text(blablacar_data.BANNER_START, size_notch=20)
b1 = page.ui.button(blablacar_data.BUTTON_FIND_RIDE, align="center").css(button_style)
b1.style.css.margin_bottom = 10

page.ui.button(blablacar_data.BUTTON_OFFER_RIDE, align="center").css(button_inv_style)

__init__.add_powered(page)
