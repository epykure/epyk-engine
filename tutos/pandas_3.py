import pandas as pd
import epyk as pk


data = {'Unemployment_Rate': [6.1, 5.8, 5.7, 5.7, 5.8, 5.6, 5.5, 5.3, 5.2, 5.2],
        'Stock_Index_Price': [1500, 1520, 1525, 1523, 1515, 1540, 1545, 1560, 1555, 1565]}

df = pd.DataFrame(data, columns=['Unemployment_Rate', 'Stock_Index_Price'])

# This can be changed to nvd3, bb, plotly, chartJs, apex or google
chart_family = "c3"

page = pk.Page()
# if you want to use Google charts you will have uncomment the below line to authorise this
#page.imports().google_products(['charts'])

template = page.body.add_template(defined_style="doc")
template.style.css.background = page.theme.greys[0]

page.ui.title("Pandas tutorial #3")
page.ui.titles.subtitle("Plot a Scatter Diagram using Pandas")
page.ui.texts.references.website(url="https://datatofish.com/plot-dataframe-pandas")

table_1 = page.ui.table(df.to_dict(orient="records"))
scatter = page.ui.charts.plot(chart_family,
  df.to_dict(orient="records"), y=["Stock_Index_Price"], x="Unemployment_Rate", kind="scatter")
row = page.ui.row([scatter, table_1])

data = {
  'Year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
  'Unemployment_Rate': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3]}

page.ui.titles.subtitle("Plot a Line Chart using Pandas")
df = pd.DataFrame(data, columns=['Year', 'Unemployment_Rate'])
table_2 = page.ui.table(df.to_dict(orient="records"))
line = page.ui.charts.plot(chart_family, df.to_dict(orient="records"), y=['Unemployment_Rate'], x="Year")
#line.options.elements.line.tension = 0
row = page.ui.row([line, table_2])

data = {'Country': ['USA', 'Canada', 'Germany', 'UK', 'France'], 'GDP_Per_Capita': [45000, 42000, 52000, 49000, 47000]}
df = pd.DataFrame(data, columns=['Country', 'GDP_Per_Capita'])

page.ui.titles.subtitle("Plot a Bar Chart using Pandas")
table_3 = page.ui.table(df.to_dict(orient="records"))
bar = page.ui.charts.plot(chart_family, df.to_dict(orient="records"), y=['GDP_Per_Capita'], x="Country", kind="bar")
row = page.ui.row([table_3, bar])

data = {'Tasks': [300, 500, 700]}
df = pd.DataFrame(data, columns=['Tasks'], index=['Tasks Pending', 'Tasks Ongoing', 'Tasks Completed'])
df = df.reset_index()

page.ui.titles.subtitle("Plot a Pie Chart using Pandas")
table_4 = page.ui.table(df.to_dict(orient="records"))
pie = page.ui.charts.plot(chart_family, df.to_dict(orient="records"), y=['Tasks'], x="index", kind="donut")
row = page.ui.row([table_4, pie])


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()
