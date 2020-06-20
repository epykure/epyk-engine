
from epyk.core.Page import Report
from epyk.core.css.themes.ThemeDark import Grey

from epyk.core.data import events
from epyk.core.data import datamap

from epyk.web import angular

#
# Create a basic report object
page = Report()
page.headers.dev()
page.theme = Grey()

#
page.ui.navigation.shortcut([
  page.ui.layouts.hr(),
  page.ui.titles.title("From to"),
  #page.ui.date(width=(100, "px")),
  page.ui.layouts.hr(),
  page.ui.titles.title("Desks"),
  page.ui.button("FX Options", htmlCode="button", icon="fab fa-angular"),
  page.ui.button("FX Options", icon="fab fa-angular"),

  #page.ui.icons.awesome("fab fa-angular").css({"right": '10px', 'position': 'absolute'}),
  page.ui.row([
    page.ui.icons.awesome("far fa-file-pdf"),
    page.ui.icons.awesome("fas fa-at"),
  ]).css({"bottom": '10px', 'position': 'absolute', 'display': 'block'})
], size=(100, 'px'), options={"position": 'left'}).add_logo("favicon.ico", path="https://www.credit-agricole.fr")

page.body.style.css.margin_left = 110

with open(r".\interactives\data\md_file.md") as f:
  content = f.read()

page.ui.text(content, htmlCode="text", options={"markdown": True})

footer = page.ui.navigation.footer('''
This is a disclaimer for mgrherhrh
''')

page.components['button'].click([
  page.js.console.log("This is atest"),
  page.components['text'].build('''
# This is a Title
''')
])

footer.style.css.padding_left = 110

# Specific to export to Angular
#app = angular.Angular(app_path=config.OUTPUT_PATHS_LOCALS_TS, name="angular")
#app.page(report=page, selector='app-root')
#app.publish()

