import sys
sys.path.append("../../epyk-ui")

from epyk.core.Page import Report
from epyk.tests import data_urls

import config

# Create a basic report object
rptObj = Report()

data_rest_1 = rptObj.py.requests.csv(data_urls.DC_QUAKES, store_location=r"C:\tmps")

# Main cross filter object
vis_dataset = rptObj.js.data.dataset(data_rest_1, "dataset1")
vis_dataview = rptObj.js.data.dataview(vis_dataset, "dataview1")


rptObj.body.onReady([
  vis_dataset, vis_dataview,

  rptObj.js.console.log(vis_dataset.distinct("status")),
  rptObj.js.console.log(vis_dataset.max("longitude")),
  rptObj.js.console.log(vis_dataview.length),
  rptObj.js.console.log(vis_dataview.getIds()),
  rptObj.js.console.log(vis_dataview.getByIds(['c821cb54-a8cd-48cb-836e-8a65c6911439'])),
])

print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_data_vis"))
