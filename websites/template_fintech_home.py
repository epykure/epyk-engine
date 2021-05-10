import epyk as pk
import __init__
from ressources import fintech_analytics


page = pk.Page()
__init__.add_banner(page, __file__)

page.ui.contents().style.css.hide()

button_css = {"border-radius": '10px', "border": '1px solid %s' % page.theme.colors[-1], 'color': page.theme.colors[-1],
              'margin-bottom': '20px'}

logo = page.ui.div(height=(30, "px"), width=(30, "px"))
logo.style.css.background_url(
  "https://raw.githubusercontent.com/epykure/epyk-ui/master/epyk/static/images/epyklogo.ico", size="auto 30px")
logo.style.css.display = "inline-block"
logo.style.css.margin_right = "10px"

company = page.ui.text("Epyk")
company.style.css.font_size = "17px"
company.style.css.font_weight = 800
company.style.css.text_transform = 'uppercase'
company.style.css.letter_spacing = '2px'

nav = page.ui.navbar(logo=page.ui.div([logo, company]), height=(80, "px"))
nav.style.css.padding_left = "30px"
nav.style.css.position = "None"

bg = page.ui.images.background(fintech_analytics.BACKGROUND_IMAGE, height=(360, "px"), position="middle")
bg.style.css.color = page.theme.colors[-1]
bg.style.css.bold()

slogan = page.ui.text(fintech_analytics.SLOGAN, align="center", width=(80, "%"))
slogan.style.css.font_size = "60px"
slogan.style.css.display = "inline-block"
slogan.style.css.margin_top = 90
bg.add(slogan)

try_epyk = page.ui.buttons.large(fintech_analytics.BUTTON_TRY)
try_epyk.css(button_css).css(
  {'color': 'white', 'background': page.theme.notch(2), 'font-size': page.body.style.globals.font.normal(8), 'margin-right': '20px'})

see_epyk = page.ui.buttons.large(fintech_analytics.BUTTON_SEE)
see_epyk.no_background()
see_epyk.css(button_css).css(
  {'background': "white", 'color': page.theme.notch(2), "border": '1px solid %s' % page.theme.notch(2),
   'font-size': page.body.style.globals.font.normal(8)})

bg.add(page.ui.div([try_epyk, see_epyk]).css({"text-align": 'center'}))

banner = page.ui.banners.text(fintech_analytics.BANNER_TEXT, size_notch=25, align="center")
banner.style.css.width = "80%"

rows, row = [], []
for ct in fintech_analytics.CONTENT:
  row.append(page.ui.vignets.vignet(title=ct["title"], icon=ct["icon"], content=ct["content"], render="row", width=(100, "%")))
  if len(row) == 2:
    rows.append(row)
    row = []
if row:
  rows.append(row)

grid = page.ui.grid(rows, width=(80, "%"))
grid.style.css.margin_bottom = 40

try_button = page.ui.button(fintech_analytics.BUTTON_TWITTER.upper(), icon="fab fa-twitter", align="center")
try_button.css(button_css)
try_button.no_background()

link = page.ui.link(fintech_analytics.LIBRARY_SPEC, url="#specTech", html_code="specTech")
link.style.css.color = "orange"

specs = page.ui.div("test")
specs.style.css.display = False

link.click([specs.dom.toggle()])
col = page.ui.col([try_button, page.ui.text(fintech_analytics.TEXT_OPENSOURCE, align="center"), link, specs])

banner = page.ui.banners.text(col, background="#fafafa")

row = [page.ui.vignets.image(title=v["title"], render="col", image=v["image"], content=v["content"]) for v in fintech_analytics.VIGNETS]
row_vignets = page.ui.row(row, width=(80, "%"), align="center")

quote = page.ui.banners.quote(fintech_analytics.QUOTE, size_notch=15, author="User feedbacks", background="#464646")
quote.style.css.color = "#bbb"
quote.style.css.padding = "40px 10%"
quote.style.css.margin = "40px 0"

about_epyk = page.ui.banners.title(fintech_analytics.BANNER_ABOUT['title'], fintech_analytics.BANNER_ABOUT['content'])
about_epyk.style.css.padding = "40px 10%"

__init__.add_powered(page)

footer = page.ui.banners.text("", background="black")
