
from epyk.core.Page import Report
from epyk.core.data import events


# Create a basic report object
page = Report()
page.headers.dev()

minimalData = {
  "teams": [
    ["Team 1", "Team 2"],
    ["Team 3", "Team 4"]
],
  "results": [
    [[1, 2], [3, 4]],
    [[4, 6], [2, 1]]]
}


bt = page.ui.lists.brackets(minimalData)
#bt.options.save([])
bt.options.onMatchHover([
  page.js.console.log(events.data)
])
bt.options.disableHighlight = True
bt.options.dir = "rl"
