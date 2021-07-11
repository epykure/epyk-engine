import pandas as pd
import epyk as pk

#  create dataframe
df = pd.DataFrame({'Sales': [50000, 122222, 2000]}, index=['TV', 'Smartphones', 'DVD'])
df.reset_index(inplace=True)
print(df.head())

page = pk.Page()
page.ui.charts.apex.donut(df.to_dict("records"), y_columns=['Sales'], x_axis="index")
page.outs.html_file(name="outDonut")
