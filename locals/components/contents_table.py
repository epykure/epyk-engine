# to be completed

from epyk.core.Page import Report


page = Report()
page.headers.dev()

# Create a content table HTML component
contents = page.ui.contents("Contente")

page.body.onReady([
  contents.build([
    {"anchor": '#test', 'level': 1, 'text': 'Ok'}
  ])
])