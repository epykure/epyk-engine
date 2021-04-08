
import pandas as pd
import numpy as np
import epyk as pk

np.random.seed(42)
df = pd.DataFrame({
  "Google": np.random.randn(1000)+0.2, "Apple": np.random.randn(1000)+0.17},
  index=pd.date_range('1/1/2000', periods=1000))
df = df.cumsum()
df = df + 50
df = df.reset_index()
df["Date"] = df["index"].dt.strftime('%Y-%m-%d')

page = pk.Page()
#page.skins.matrix()

page.ui.title("Pandas tutorial #1")
page.ui.texts.references.github("https://github.com/PatrikHlobil/Pandas-Bokeh")
template = page.body.add_template(defined_style="doc")
template.style.css.background = page.theme.greys[0]

page.ui.titles.subtitle("Google versus Apple")
page.ui.charts.apex.line(df.to_dict(orient="records"), y_columns=["Google", "Apple"], x_axis="Date")

df = pd.DataFrame({"Animal": ["Mouse", "Rabbit", "Dog", "Tiger", "Elefant", "Wale"],
                   "Weight [g]": [19, 3000, 40000, 200000, 6000000, 50000000]})

line = page.ui.charts.apex.line(df.to_dict(orient="records"), y_columns=["Weight [g]"], x_axis="Animal")
line.options.xaxis.title.text = "Animals"
line.options.yaxis.title.text = "Weight"
scatter = page.ui.charts.apex.scatter(df.to_dict(orient="records"), y_columns=["Weight [g]"], x_axis="Animal")
scatter.options.xaxis.title.text = "Animals"
scatter.options.yaxis.title.text = "Weight"
scatter.options.yaxis.labels.formatters.scale(1000000)
page.ui.row([line, scatter])

data = {
    'fruits': ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries'],
    '2015': [2, 1, 4, 3, 2, 4],
    '2016': [5, 3, 3, 2, 4, 6],
    '2017': [3, 2, 4, 4, 5, 3]
}
df = pd.DataFrame(data)

page.ui.titles.subtitle("Fruit price per year")
bar = page.ui.charts.apex.bar(df.to_dict(orient="records"), y_columns=["2015", "2016", "2017"], x_axis="fruits")
bar.colors(["blue", "green", "orange"])

page.ui.layouts.hr()
page.ui.titles.subtitle("Report powered by")
page.ui.rich.powered()


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()
