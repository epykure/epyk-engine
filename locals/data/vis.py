
import epyk as pk

from epyk.mocks import urls as data_urls


# Create a basic report object
page = pk.Page()
page.headers.dev()

data_rest_1 = page.py.requests.csv(data_urls.DC_QUAKES)

# Main cross filter object
vis_dataset = page.js.data.dataset(data_rest_1, "dataset1")
vis_dataview = page.js.data.dataview(vis_dataset, "dataview1")

page.body.onReady([
  vis_dataset, vis_dataview,

  page.js.console.log(vis_dataset.distinct("status")),
  page.js.console.log(vis_dataset.max("longitude")),
  page.js.console.log(vis_dataview.length),
  page.js.console.log(vis_dataview.getIds()),
  page.js.console.log(vis_dataview.getByIds(['c821cb54-a8cd-48cb-836e-8a65c6911439'])),
])

