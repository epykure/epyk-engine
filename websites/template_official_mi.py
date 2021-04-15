import epyk as pk
from ressources import link_data


page = pk.Page()
page.ui.contents().style.css.hide()
nav = page.ui.navbar(height=(40, "px"))
nav.style.css.padding_left = "30px"
nav.style.css.position = "None"

row = []
for item in link_data.MI_ITEMS:
  row.append(page.ui.col([
    page.ui.img(item['img'], path=link_data.MI_ITEM_PATH, width=(40, "px")),
    page.ui.text(item['text'], align="center")]))

row = page.ui.row(row)
row.style.css.margin = "20px auto"

vignets = []
for v in link_data.MI_VIGNETS:
  vignets.append(
    page.ui.vignets.image(title=v['title'], image=v['image'], content=page.py.encode_html(v['content']), render="col"))
  vignets[-1].add(
    page.ui.link("Join now >").css({"display": 'block', 'text-align': 'left', 'padding': '10px 15px 0 15px'}))
row = page.ui.row(vignets)

image = page.ui.images.background("%s%s" % (link_data.MI_ITEM_PATH, link_data.MI_XBOX), height=(500, "px"))
page.ui.title("For Work").css({"margin": '20px 5% 0 5%'})
page.ui.vignets.background("%s%s" % (link_data.MI_ITEM_PATH, link_data.MI_REMOTE))
page.ui.banners.follow("Follow Microsoft", width=(90, "%"))
page.ui.banners.row(link_data.MI_ROW_HEADERS, link_data.MI_ROW_LINKS)
page.ui.banners.disclaimer(link_data.MI_DISCLAIMER_TEXT, links=link_data.MI_DISCLAIMER_LINKS)
