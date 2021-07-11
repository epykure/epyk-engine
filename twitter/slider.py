import epyk as pk
import pandas as pd
from epyk.tests import data_urls

page = pk.Page()
# Use a pandas dataframe from external resources.
records = pd.DataFrame(page.py.requests.csv(data_urls.C02_DATA))
records["year"] = records["year"].astype(int)
records["population"] = pd.to_numeric(records['population'], errors='coerce', downcast="integer")
reduce_data = records[(records["year"] > 1990) & (~ records.country.isin(["World", "Europe", "North America"]))]
reduce_data = reduce_data.fillna(0)
# Create a JavaScript filtering group
grp = page.data.js.record(reduce_data.to_dict("records")).filterGroup("aggData")
title = page.ui.title("CO2 Data")  # Add a title component
select = page.ui.fields.select(  # Add select component
  pk.inputs.select.from_list(reduce_data["year"].unique()[::-1]), label="Country")
# Add a slider range object and a bar chart from ChartJs
slider = page.ui.sliders.range(
  minimum=int(min(reduce_data["population"])), maximum=int(max(reduce_data["population"])))
bar = page.ui.charts.bar(y_columns=["primary_energy_consumption"], x_axis=["country"])
# Add event for interactivity
select.input.change([  # Filter data and update the chart
  bar.build(grp.equal("year", select.input.dom.content).sup("population", slider.dom.min_select).
    inf("population", slider.dom.max_select).group().sumBy(
      ["primary_energy_consumption"], ['country'], cast_vals=True))
])
slider.change([  # reuse the previous event
  select.input.dom.events.trigger("change")
])
page.outs.html_file(name="outSlider")
