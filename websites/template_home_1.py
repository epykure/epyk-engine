
import epyk as pk
from ressources import fintech_analytics


page = pk.Page()
page.body.style.globals.font.size = 18

page.ui.banners.corner("Webtemplate", position="top")
page.ui.contents().style.css.hide()

grp1 = page.ui.texts.button("Home")
grp2 = page.ui.texts.button("Group")

nav = page.ui.navbar()
nav.add(grp1)
nav.add(grp2)

page.ui.images.wallpaper(r"https://images.pexels.com/photos/1376124/pexels-photo-1376124.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500", height=(80, "%"))

banner = page.ui.banners.title(title=fintech_analytics.SLOGAN, content=fintech_analytics.BANNER_ABOUT['content'])
banner.style.css.margins(0, right=(10, '%'), left=(10, '%'))

banner.content[1].style.css.text_align = "justify"

name = page.ui.title("Present to users", align="center")
scene = page.ui.img("https://images.pexels.com/photos/952422/pexels-photo-952422.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500")
name2 = page.ui.title("Advertise work", align="center")
private = page.ui.img("https://images.pexels.com/photos/1540338/pexels-photo-1540338.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500")
name3 = page.ui.title("Celebrate Success", align="center")
club = page.ui.img("https://images.pexels.com/photos/342520/pexels-photo-342520.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500")

row = page.ui.div([[name, scene], [name2, private], [name3, club]], position="top")
row[0].style.css.inline_block(width=(32, "%"))
row[0].style.css.text_align = "center"
row[0].style.css.padding = "0 1%"
row[1].style.css.inline_block(width=(32, "%"))
row[1].style.css.text_align = "center"
row[1].style.css.padding = "0 1%"
row[2].style.css.inline_block(width=(32, "%"))
row[2].style.css.text_align = "center"
row[2].style.css.padding = "0 1%"
row.style.css.margins(0, right=(5, '%'), left=(5, '%'))

img1 = page.ui.img("https://images.pexels.com/photos/106344/pexels-photo-106344.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500")
img2 = page.ui.img("https://images.pexels.com/photos/6224/hands-people-woman-working.jpg?auto=compress&cs=tinysrgb&dpr=2&w=500")
img3 = page.ui.img("https://images.pexels.com/photos/3184465/pexels-photo-3184465.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500")

title1 = page.ui.title("Scenes", align="center")
title2 = page.ui.title("Scenes", align="center")
title3 = page.ui.title("Scenes", align="center")

b1 = page.ui.buttons.colored("Details", align="center")
b1.style.css.padding_top = 5
b1.style.css.padding_bottom = 5
b2 = page.ui.buttons.colored("Details", align="center")
b2.style.css.padding_top = 5
b2.style.css.padding_bottom = 5
b3 = page.ui.buttons.colored("Details", align="center")
b3.style.css.padding_top = 5
b3.style.css.padding_bottom = 5

t1 = page.ui.title("Easy Dashboarding", align="center")
t2 = page.ui.title("Collaborate more", align="center")
t3 = page.ui.title("Get users feedbacks", align="center")

div1 = page.ui.div([t1, b1])
div1.style.css.background = "white"
div1.style.css.padding = 10

div2 = page.ui.div([t2, b2])
div2.style.css.background = "white"
div2.style.css.padding = 10

div3 = page.ui.div([t3, b3])
div3.style.css.background = "white"
div3.style.css.padding = 10

row = page.ui.div([[title1, img1, div1], [title2, img2, div2], [title3, img3, div3]])
row.style.css.margins(0, right=(5, '%'), left=(5, '%'))
row[0].style.css.inline_block(width=(33, "%"))
row[0].style.css.padding = "10px 5%"
row[1].style.css.inline_block(width=(33, "%"))
row[1].style.css.padding = "10px 5%"
row[2].style.css.inline_block(width=(33, "%"))
row[2].style.css.padding = "10px 5%"

paragraph = page.ui.texts.paragraph(fintech_analytics.QUOTE)
paragraph.style.css.color = page.theme.greys[-2]
paragraph.style.css.padding = "0 10%"

banner = page.ui.banners.title(title=fintech_analytics.BANNER_TEXT, content=[paragraph, row])
banner.style.css.margin_top = 20
banner.style.css.background = "black"
banner.style.css.text_align = "center"

ic1 = page.ui.icons.twitter()
ic2 = page.ui.icons.facebook()
ic3 = page.ui.icons.instagram()
ic4 = page.ui.icons.linkedIn()
ic5 = page.ui.icons.youtube()

banner = page.ui.banners.title(title="Contacts", content=page.ui.div([ic1, ic2, ic3, ic4, ic5], align="center"))
banner.style.css.margin_top = 20


row.options.responsive = False
row.options.autoResize = False
