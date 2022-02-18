
import epyk as pk


page = pk.Page()
page.headers.dev()

data = [
    {"id": 0, "group": 0, "content": 'item 0', "start": "2020-06-29", 'type': 'point'},
    {"id": 0, "group": 0, "content": 'item 0', "start": "2020-06-17", "end": "2020-06-21", 'className': 'red'},
    {"id": 1, "group": 0, "content": 'item 1', "start": "2020-06-10", "end": "2020-06-20", 'type': 'background'},
    {"id": 2, "group": 1, "content": 'item 2', "start": "2020-06-16", "end": "2020-06-24", 'className': 'red'},
    {"id": 3, "group": 1, "content": 'item 3', "start": "2020-06-23", "end": "2020-06-24", 'type': 'box'},
    {"id": 4, "group": 1, "content": 'item 4', "start": "2020-06-24", "end": "2020-06-26", 'className': 'orange'},
    {"id": 5, "group": 2, "content": 'item 5', "start": "2020-06-24", "end": "2020-06-27"}
  ]

groups = [
  {"id": 1, 'content': 'test 1'},
  {"id": 2, 'content': 'test 2'},
  {"id": 3, 'content': 'test 3'},
  {"id": 0, 'content': 'test 0'},
]

timeline2 = page.ui.charts.vis.timeline(data, content="content", start='start', end="end", type="type", group="group")
#timeline2.options.stack = True
timeline2.options.editable = False
timeline2.setGroups(groups)

timeline2.addClassName('orange', {
  'background-color': 'orange', 'color': 'white'
}, {'background-color': 'green', 'color': 'black'})



timeline2.addClassName('red', {
  'background-color': 'red', 'color': 'white'
}, {'background-color': 'white', 'color': 'black'})

timeline2.onReady([
  timeline2.js.addCustomTime("2020-07-03", 'test'),
  timeline2.js.addCustomTime("2020-07-05", 'ok'),
  timeline2.js.setCustomTimeTitle("This is a test", 'ok'),

])

page.ui.button("click").click([
  timeline2.js.setCustomTimeMarker("This is a test", 'ok')
  #timeline2.js.removeCustomTime('test2')
])
