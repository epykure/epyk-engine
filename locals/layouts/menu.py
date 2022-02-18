
import epyk as pk


# Create a basic report object
page = pk.Page()
page.headers.dev()

#page.theme = ThemeDark.Grey()
record = [{"text": "Lin 1", 'url': 'report_list.html'}, {"text": "Link 2"}]
page.ui.navigation.pin("anchor", tooltip="test", bottom=20)
#page.ui.text("test").css({"display": 'inline-block'})
#page.ui.text(page.symbols.shapes.BLACK_RIGHT_POINTING_TRIANGLE).css({"display": 'inline-block'})
#page.ui.text("test").css({"display": 'inline-block'})


mb = page.ui.menus.button("Value", page.ui.list(["value 1", "value 2"]))
mb.items[0].click([page.js.alert(mb.items[0].dom.content)])

page.ui.images.badge(12, icon="far fa-bell", options={"badge_position": 'right'})

tb = page.ui.menus.toolbar(["fas fa-paint-brush", "fas fa-code"])
tb[1].link.val = 4589
tb[1].tooltip("This is a tooltip")
tb[0].style.css.color = 'red'

ds = page.ui.menus.divisor(["Link 1", 'Link 2', 'Link 3'])
ds.texts[0].click([
  page.js.alert(ds.texts[0].dom.content)
])

bs = page.ui.menus.buttons(["Button", "Button 2", "Button 3"])
bs[2].click([
  page.js.alert(bs[2].dom.content)
])

# page.ui.div(
#   [page.ui.text("test 1"),
#    [page.ui.text("test2", width=None), page.ui.text("test3", width=None)]]
# )


record = [
  {"value": 'A', 'title': 'Title', 'children': [
    "item 1",
    "item 2",
    "item 3",
  ]},
  {"value": 'B', 'title': 'Title 2', 'children': [
    "item 1",
    "item 2",
    "item 3",
  ]},
  {"value": 'C', 'title': 'Title 3', 'children': [
    [
    "item C",
    "item 2",
    "item 3"],
    [
      "item 424",
    ]
  ]},
  {"value": 'D', 'title': 'Title 4', 'children': [
    "item C",
    "item 2",
    "item 3",
  ]},
]

#top = page.ui.menus.menu(record,
#      options={"li_css": {"color": 'white', "padding": '5px 16px', "display": 'inline-block'},
#        "li_class": ["CssDivOnHoverBackgroundLight", "CssTextNotSelectable"],
#      })
#      })

div = page.ui.div(width=(100, "px"))
div.style.css_padding_left = "5px"
div.style.css_margin_top = 5

for i in range(5):
  item = page.ui.div("Menu %s" % i).css({"padding": "1px 10px", "margin": "2px 0", "color": page.theme.colors[7],
                                           "border-left": "1px solid %s" % page.theme.greys[0]})
  item.attr["name"] = div.htmlCode
  item.style.add_classes.div.background_hover()
  item.click([
    item.dom.by_name.css({"border-left": "1px solid %s" % page.theme.greys[0], "color": page.theme.colors[7]}).r,
    item.dom.css({"border-left": "1px solid %s" % page.theme.success[1], "color": page.theme.colors[-1]})
  ])
  item.options.managed = False
  div + item

