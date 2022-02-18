
import epyk as pk

#
from epyk.mocks import randoms


# Create a basic report object
page = pk.Page()
page.headers.dev()

# Console component
c = page.ui.rich.console(
  "* This is a log section for all the events in the different buttons *", options={"timestamp": True})

#
jsData = page.data.js.record('data_test', randoms.languages)
filter = jsData.filterGroup("test")


page.body.onReady([
  #
  #filter.equal('y', 25).startswith('text', 'test').setFilter("filterTest"),

  #page.js.console.log(jsData.getFilter('filterTest')),
  #page.js.console.log(jsData.getFilter('filterTest').group().count(["x", "y", "y1"], attrs={"name": 'ok'})),
  c.dom.write(filter.group().max("rating"), stringify=True),
  c.dom.write(filter.group().min("rating"), stringify=True),
  c.dom.write(filter.group().sortBy("change")[-1].defaults({"toto": 1}), stringify=True),
  c.dom.write(filter.group().pluck("name"), stringify=True),
  # '''function filterOption2(r, k, v){var n=[];r.forEach(function(e){if(e[k]==v){n.push(e)}});return n};
  # ''',
  # '''
  # var dataPoints = [
  # {'x': 0, 'y': 10, 'y1': 10},
  # {'x': 1, 'y': 35, 'y1': 20},
  # {'x': 2, 'y': 25, 'y1': 10},
  # {'x': 3, 'y': 30, 'y1': 5},
  # {'x': 4, 'y': 28, 'y1': 10}]
  #
  # ''',
  # 'console.log( filterOption(dataPoints, ["y"], "x") )',
  #page.js.console.log("dataPoints", skip_data_convert=True)
  #js_data.clearFilters()
])

