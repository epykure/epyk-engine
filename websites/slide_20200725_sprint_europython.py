
import epyk as pk
import __init__

from ressources import blablacar_data
from epyk.tests import mocks, data_urls

import random

page = pk.Page()
__init__.add_banner(page, __file__, "top")

#
data_rest = page.py.requests.csv(data_urls.PLOTLY_APPLE_PRICES)
page.body.style.globals.size = 18
contents = page.ui.contents("Contents", top=50, right=50)
slides = page.ui.vignets.slides(start=0, options={"timer": 2, 'contents': contents})
slides.style.css.display = "block"
slides.add_slide("Epyk - A Web Studio library", [
  page.ui.title('''A centralise library to control your whole stack''', level=2),
  page.ui.layouts.new_line(2),
  page.ui.img("epyklogo_whole_big.png?raw=true", path="https://github.com/epykure/epyk-ui/blob/master/epyk/static/images/", width=(300, 'px')),
], options={"contents_title": 'Test', "contents_level": 2})

slides.add_slide("Epyk - Images", [
  page.ui.images.carousel(["1-1-hubble-z3-black-gray-family-img.jpg", "1-4-hubble-y2-cloud-blue-closeup-img.jpg", "1-5-hubble-z3-gray-closeup-img.jpg"],
                           path="https://images.samsung.com/mk/smartphones/galaxy-s20/buy/carousel/pc", options={"arrows": True, 'points': False})
])

slides.add_slide("Epyk - Architecture", [
    page.ui.img("architecture.PNG?raw=true", path="https://github.com/epykure/epyk-ui/blob/master/epyk/static/images", width=(500, 'px'))
])


slides.add_slide('Epyk - Simple rules', [
   page.ui.title('Easy to write code'),
   page.ui.texts.paragraph('''The philosophy behind the library structure is to allow both novice and advance developers to be able to start
   implementing their full stack solution really easily. In that effect novice developers don't have to write a lot of code before being able to
   implementing their solutions.
   On the other side more senior developers can deep dive into the library and start leveraging on the capabilities of javascript and all the other tools
   integrated in this framework''', width=500),
   page.ui.title('No dogma'),
   page.ui.texts.paragraph('''In order to let everyone find whatever they're looking for when using a "transpiling" library, we tried to make the
   library compatible with the most framework possible. Thanks to this, people coming from a front end development background will be able to
   easily find their marks. We're also very interested in their feedback in order to improve the solution as a whole''', width=500),
],)

col = page.ui.col([
  page.ui.text("Toto", align="center"),
  page.ui.text("Toto 2 ", align="center")
])

slides.add_slide("Epyk Studio - Ambition", [
    page.ui.row([
        page.ui.vignets.vignet(title='Core Library', content='''Improve and leverage on existing web framework to offer a maximum of features to developers'''),
        page.ui.vignets.vignet(title='Mobile Expansion', content=col),
        page.ui.vignets.vignet(title='Knowledge Sharing', content='''In addition to the documentation, we have put in a place a huge number of notebooks for people to use as a knowledge base''')
    ], align="center", position="top")
])

row = []
for k, v in blablacar_data.CATEGORIES.items():
    row.append(page.ui.vignets.vignet(title=k, content=v))

button_style = {"border-radius": '20px', 'background-color': 'rgb(0, 175, 245)', 'color': 'white', 'padding': '8px 25px', 'font-size': '18px'}
button_inv_style = {"border-radius": '20px', 'background-color': 'white', 'color': 'rgb(0, 175, 245)', 'padding': '8px 25px', 'font-size': '18px'}
title_style = {"width": '90%', 'margin': 'auto', 'font-weight': 800, 'line-height': '1.06', 'font-size': '30px', 'color': 'rgb(5, 71, 82)', 'padding': '24px 0px'}

button = page.ui.button(blablacar_data.BUTTON_OFFER_RIDW, align="center")
button.style.css.margin_top = 10
button.css(button_style)

content = page.ui.col([page.ui.text(blablacar_data.SLOGAN, width=(100, "%")), button])
content.style.css.padding = 0

slides.add_slide('Epyk - Code Sample - 1', [
  page.ui.title('Only a few lines of code allow to generate a complete working page', level=2),
  page.ui.layouts.new_line(),
  page.ui.img("macdonalds.PNG?raw=true", path="https://github.com/epykure/epyk-ui/blob/master/epyk/static/images/", width=(600, 'px')),
  page.ui.layouts.new_line(2),
  page.ui.img("macdonalds_results.PNG?raw=true", path="https://github.com/epykure/epyk-ui/blob/master/epyk/static/images/", width=(600, 'px')),]
)

slides.add_slide("Epyk - Code Sample - 2", [
    page.ui.title("Car Company").css({"margin-top": '130px'}),
    page.ui.vignets.image(blablacar_data.VIGNET_2['title'], content=content, image=blablacar_data.VIGNET_2['image']),
    page.ui.titles.title(blablacar_data.TITLE_1).css(title_style),
    page.ui.row(row, align="center", position="top")
])

c = page.ui.charts.chartJs.line(mocks.languages, y_columns=["rating", 'change'], x_axis='name')
c.dragData()

# Using standard Javascript Libraries
slides.add_slide("Epyk - Analytics", [
  page.ui.row([
    page.ui.charts.chartJs.bar(data_rest, y_columns=['AAPL.Open'], x_axis="Date"),
    page.ui.charts.chartJs.timeseries(data_rest, y_columns=['AAPL.Open'], x_axis="Date")
  ]),
  c
])

# # -------------------------
# # Of course using the underlying Dash library
data_rest = page.py.requests.csv(data_urls.PLOTLY_3D)
#
slides.add_slide("Epyk - Plotly", [
  page.ui._3d.plotly.ribbon(data_rest, y_columns=["y1"], x_axis='x1', z_axis="z1", width=(600, 'px'))
])

# # -------------------------
# # Ceinralise your team work for free
data = [
    {"id": 0, "group": 0, "content": 'item 0', "start": "2020-06-29", 'type': 'point'},
    {"id": 0, "group": 0, "content": 'item 0', "start": "2020-06-17", "end": "2020-06-21"},
    {"id": 1, "group": 0, "content": 'item 1', "start": "2020-06-10", "end": "2020-06-20", 'type': 'background'},
    {"id": 2, "group": 1, "content": 'item 2', "start": "2020-06-16", "end": "2020-06-24"},
    {"id": 3, "group": 1, "content": 'item 3', "start": "2020-06-23", "end": "2020-06-24", 'type': 'box'},
    {"id": 4, "group": 1, "content": 'item 4', "start": "2020-06-24", "end": "2020-06-26"},
    {"id": 5, "group": 2, "content": 'item 5', "start": "2020-06-24", "end": "2020-06-27"}
  ]

groups = [
  {"id": 1, 'content': 'test 1'},
  {"id": 2, 'content': 'test 2'},
  {"id": 3, 'content': 'test 3'},
  {"id": 0, 'content': 'test 0'},
]

timeline2 = page.ui.charts.vis.timeline(data, content="content", start='start', end="end", type="type", group="group", options={"type": 'box'})
timeline2.options.stack = True
timeline2.setGroups(groups)
#
rows = []
#rows.append(page.ui.row(["Category", "", "Timelines", "Progression", "", "", "", "Status", "Activity", "Files"]))
rows.append(["Category", "", "Timelines", "Progression", "", "", "", "Status", "Activity", "Files"])

for i in range(10):
  rows.append([
    page.ui.div("This is a text").css({"border-left": '1px solid %s' % page.theme.success[1], 'padding-left': '10px', 'background': page.theme.success[0]}),
    page.ui.timelines.view("2020-01-05", "2020-%s-%s" % (random.randint(1, 12), random.randint(1, 25))),
    page.ui.sliders.progress(random.randint(1, 100)),
    page.ui.charts.sparkline("line", [random.randint(1, 25) for i in range(10)], width=("40", 'px')),
  ])

slides.add_slide("Epyk - Time Tracker (Agile Teams)", [
  timeline2,
  page.ui.grid(rows)
])

slides.add_slide("Epyk - Where to find it ?", [
    page.ui.title('Come take a look and maybe participate !', level=1),
    page.ui.layouts.new_line(1),
    page.ui.list([
      page.ui.links.link('Pypi', 'https://pypi.org/project/epyk/', icon='fab fa-python'),
      page.ui.links.link('Github', 'https://github.com/epykure/epyk-ui', icon='fab fa-github'),
      page.ui.links.link('Documentation', 'http://www.epyk.io/', icon='fa fa-book'),
      page.ui.links.link('Templates', 'https://github.com/epykure/epyk-templates', icon='fa fa-file'),
      page.ui.links.link('epykachu@gmail.com', 'epykachu@gmail.com', icon='fa fa-envelope'),
  ])
])

sp = page.ui.banners.sponsor(["BFM-Business.png", '20-MIN.png', 'microsoft.jpg'])

__init__.add_powered(page)

#page.ui.button("Click").click([
#  slides.dom.goTo(5)
#])
#
# page.body.onReady([
#   contents.build([{"anchor": '#test', 'level': 1, 'text': 'Overview'}])
# ])
