
import pandas as pd
import numpy as np
import epyk as pk

ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
ts = ts.cumsum()
df = ts.reset_index()
df["index"] = df["index"].dt.strftime('%Y-%m-%d')

page = pk.Page()
page.ui.title("Pandas tutorial #2")
template = page.body.add_template(defined_style="doc")
template.style.css.background = page.theme.greys[0]

page.ui.texts.references.website(url="https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html")
page.ui.charts.chartJs.line(df.to_dict(orient="records"), y_columns=[0], x_axis="index")

df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list("ABCD"))
df = df.cumsum()
df = df.reset_index()
df["index"] = df["index"].dt.strftime('%Y-%m-%d')

lines = page.ui.charts.chartJs.line(df.to_dict(orient="records"), y_columns=list("ABCD"), x_axis="index")
lines.options.elements.point.radius = 0
lines.options.tooltips.callbacks.labelNumber(digit=2)
lines.options.tooltips.intersect = False
lines.options.tooltips.mode = "index"

df3 = pd.DataFrame(np.random.randn(1000, 2), columns=["B", "C"]).cumsum()
df3["A"] = pd.Series(list(range(len(df))))

line3 = page.ui.charts.chartJs.line(df3.to_dict(orient="records"), y_columns=["B"], x_axis="A")
line3.options.elements.point.radius = 0

df4 = pd.DataFrame(np.random.rand(10, 4), columns=["a", "b", "c", "d"])
df4 = df4.reset_index()
bar = page.ui.charts.chartJs.bar(df4.to_dict(orient="records"), y_columns=["a", "b", "c", "d"], x_axis="index")

bar.options.scales.xAxes.stacked = True
bar.options.scales.yAxes.stacked = True
bar.options.tooltips.callbacks.labelNumber(digit=2)

hbar = page.ui.charts.chartJs.hbar(df4.to_dict(orient="records"), y_columns=["a", "b", "c", "d"], x_axis="index")
hbar.options.tooltips.callbacks.labelNumber(digit=2)

row = page.ui.row([bar, hbar])
row.options.responsive = False
row.options.autoSize = False

df5 = pd.DataFrame(np.random.rand(10, 4), columns=["a", "b", "c", "d"])
df5 = df5.reset_index()
area = page.ui.charts.chartJs.area(df5.to_dict(orient="records"), y_columns=["a", "b", "c", "d"], x_axis="index")
area.colors(["red", "orange", "yellow", "blue"])
area.options.scales.xAxes.stacked = True
area.options.scales.yAxes.stacked = True
area.options.tooltips.callbacks.labelNumber(digit=2)

scatter = page.ui.charts.chartJs.scatter(df5.to_dict(orient="records"), y_columns=["b", "c", "d"], x_axis="a")
scatter.options.scales.xAxes.scaleLabel.label("XAxis")
scatter.options.scales.yAxes.scaleLabel.label("YAxis")

series = pd.Series(3 * np.random.rand(4), index=["a", "b", "c", "d"], name="series")
df6 = series.reset_index()
pie = page.ui.charts.chartJs.pie(df6.to_dict(orient="records"), y_columns=["series"], x_axis="index")

page.ui.layouts.hr()
page.ui.titles.subtitle("Report powered by")
page.ui.rich.powered()
