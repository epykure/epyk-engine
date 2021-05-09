
import epyk as pk


# Test module to get test data
from epyk.tests import mocks


page = pk.Page()
page.headers.dev()

page.ui.hidden("Test")

input = page.ui.input()
chips = page.ui.select(pk.inputs.select.from_records(mocks.languages, column="type"))

#
filters = page.ui.panels.filters()

filter = page.data.js.record(data=mocks.languages).filterGroup("test")
filter2 = page.data.js.record(data=mocks.languages).filterGroup("test2")

c = page.ui.charts.chartJs.bubble(mocks.languages, y_columns=["rating", 'change'], x_axis='name')
c.label(0, "New Test label")

data = [{"label": "python", "value": False}, {"label": "Java", "value": 5}]
checks1 = page.ui.lists.checks(data)

c_data = pk.inputs.check.from_records(mocks.languages, "name")
checks2 = page.ui.lists.checks(c_data, options={"checked": True})

checks2.click([
  page.js.console.log(page.js.objects.value),
  c.build(filter.includes('name', checks2.dom.content)),
  #page.js.console.log(page.js.objects.value),
  #c.build(filter.equal('name', page.js.objects.value)),
])

page.ui.button("Test").click([
  page.js.console.log(checks1.dom.content),
  page.js.console.log(checks2.dom.content),
])

d = page.ui.drawer()

select_all = page.ui.button("Select")
select_all.click([
  checks2.dom.selectAll(),
  c.build(filter.includes('name', checks2.dom.content)),
])

unselect_all = page.ui.button("UnSelect")
unselect_all.click([
  checks2.dom.unSelectAll(),
  c.build(filter.includes('name', checks2.dom.content, empty_all=False)),
])

d.add_panel([
  page.ui.titles.headline("Columns"),
  select_all, unselect_all,
  checks2], [c], display='block')

#chips.delete([
  #page.js.console.log(chips.dom.values()),
#  c.build(filter.includes('label', chips.dom.values())),
#])

chips.change([
  #page.js.console.log(chips.dom.values()),
  c.build(filter.equal('name', input.dom.content)),
  c.build(filter.equal('type', chips.dom.content)),
])

# filters
input.enter([
  filters.dom.add(input.dom.content, 'name'),
  c.build(filter2.match(filters.dom.content, case_sensitive=False)),

])

page.ui.button("reset").click([
  c.build(filter.equal('label', input.dom.content)),
  #c.js.render(),
])

page.ui.button("add").click([
  #c.js.add('point', {'Test': 28}),
  #c.js.update(),
  c.js.remove(0, ["Test"]),
  c.js.load("Test2", [{'x': 0, 'y': 23}, {'x': 1, 'y': 23}]),
  c.js.unload(),
  c.js.update()
  #c.js.render(),
])

c.click([
  page.js.console.log(c.js.content)
])

dataPoints3 = [
  {'label': "mango", 'x': 0, 'y': 20, 'y1': 20, 'r': 10},
  {'label': "grape", 'x': 1, 'y': 18, 'y2': 20, 'r': 5}
]

page.ui.button("reset").click([
  c.build(dataPoints3),
  #c.build(dataPoints3, options={'z_columns': ['r']}),
  #c.js.render(),
])

