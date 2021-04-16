
import epyk as pk
from ressources import link_data


page = pk.Page()
page.ui.contents().style.css.hide()
page.body.style.css.background = '#F2F2F2'

navbar = page.ui.navbar()
navbar.style.css.background_color = '#fecc00'

page.body.add_template(defined_style="margins")
car = page.ui.images.background(link_data.CARROUSEL[0], height=(350, "px"), size="contain")
car.style.css.margin_top = 10
#
title = page.ui.title(page.py.encode_html(link_data.CINEMA), align="center").css({"margin": '20px 1% 0 1%'})
title.style.css.font_factor(25)

row = []
for grp in link_data.CINE_GROUPS:
  row.append(page.ui.col([page.ui.div([
    page.ui.div("#").css({"color": '#fecc00', 'width': 'auto', 'display': 'inline-block'}).style.css.font_factor(6),
    page.ui.subtitle(page.py.encode_html(grp)).css({"white-space": 'nowrap','width': 'auto', 'display': 'inline-block'}),
  ]).css({"white-space": 'nowrap'})], align="center"))
page.ui.row(row)

#
page.ui.title(page.py.encode_html(link_data.NEW_CINE)).css({"margin": '20px 1% 0 1%'})

vignets = []
for v in link_data.VIGNETS:
  vignets.append(page.ui.vignets.image(title=page.py.encode_html(v['title']), image=v['image'], content=page.py.encode_html(v['content']), render="col"))
row = page.ui.row(vignets)

but = page.ui.forms.subscribe()
but.button.click([page.js.alert(but.input.dom.content)])

about = page.ui.banners.contact_us()
about.button.click([
  page.js.console.log(about.dom.val)
])

