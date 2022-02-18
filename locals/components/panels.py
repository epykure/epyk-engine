
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

p = page.ui.panels.pills()
p.add_panel("Pill 1", page.ui.col([page.ui.text("test 1")]))
p.add_panel("Pill 2", page.ui.col([page.ui.text("test 2")]), selected=True)
p.add_panel("Pill 3", page.ui.col([page.ui.text("test 3")]))

tabs = page.ui.panels.arrows_down()
tabs.add_panel("tab 1, this is something", page.ui.col([page.ui.text("test 1, this is for something")]))
tabs.add_panel("tab 2", page.ui.col([page.ui.text("test 2")]), icon="fab fa-500px")
tabs.add_panel("tab 3", page.ui.col([page.ui.text("test 3")]))


tabs = page.ui.panels.arrows_up()
tabs.add_panel("tab 1, this is something", page.ui.col([page.ui.text("test 1, this is for something")]))
tabs.add_panel("tab 2", page.ui.col([page.ui.text("test 2")]))
tabs.add_panel("tab 3", page.ui.col([page.ui.text("test 3")]))


page.ui.panels.sliding([
  page.ui.col([page.ui.text("test 2")])
], title="Sliding Panel")


split_panel = page.ui.panels.split()
split_panel.left(page.ui.col([page.ui.text("Left")]))
split_panel.right(page.ui.col([page.ui.text("Right")]))

