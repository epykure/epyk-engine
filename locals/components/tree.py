
from epyk.core.Page import Report


page = Report()
page.headers.dev()

# Console component
c = page.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

# #
data = [{"label": 'test', 'items': [{"label": 'child 1', 'color': 'red'}]}]
#
# #
#tree1 = page.ui.lists.tree(data)
#
# #
# tree2 = page.ui.trees.tree(data)
#
# #
# tree3 = page.ui.trees.inputs(data)

#
data2 = [
  {"value": 'test 1'},
  {"value": 'test', 'items': [
    {"value": 'child 1', 'color': 'red', 'items': [
        {"value": 'Sub child 2', 'color': 'red', 'items': [
            {"value": 'sub sub child 2', 'color': 'red'},
        ]},
    ]},
    {"value": 'child 2', 'color': 'red', 'items': [
        {"value": 'sub child 2 1', 'color': 'red'},
        {"value": 'sub child 2 2', 'color': 'red', 'items': [
            {"value": 'sub child 2 2 1', 'color': 'red'},
            {"value": 'sub child 2 2 2', 'color': 'red'},
        ]},
        {"value": 'sub child 2 3', 'color': 'red'},
        {"value": 'sub child 2 4', 'color': 'red'},
    ]},
    {"value": 'child 3', 'color': 'red'},
  ]}
]

#
tree2 = page.ui.trees.tree(data2)

tree5 = page.ui.buttons.menu(["A", "B", "C"])

tree5[0].on('click', [
  page.js.alert("Ok"),
  tree5[1].js.set_url("https://stackoverflow.com/questions/5220852/anyway-to-change-href-of-link-with-no-id-and-no-jquery")
])

#
page.ui.buttons.colored("click", align="center").click([
  tree5[1].js.set_text("Test")
])

c.move()

