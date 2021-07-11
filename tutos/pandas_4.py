import pandas as pd
import epyk as pk
import numpy as np

page = pk.Page()

# if you want to use Google charts you will have uncomment the below line to authorise this
#page.imports.google_products(['charts'])

#
template = page.body.add_template(defined_style="doc")
template.style.css.background = page.theme.greys[0]

# This can be changed to nvd3, c3, billboard, plotly, chartJs, apex or google
chart_family = "bb"

page.ui.title("Pandas tutorial #4")

s1 = page.ui.titles.subtitle("Plot using various charting libraries (with %s)" % chart_family)
s2 = page.ui.text("Framework compatible with nvd3, c3, billboard, plotly, chartJs, apex or google charts.")

div = page.ui.div([s1, s2])
div.style.css.border = "1px solid %s" % page.theme.notch()
div.style.css.padding = 5

day_num = np.linspace(1, 10, 10)
daily_words = [450, 628, 488, 210, 287, 791, 508, 639, 397, 943]
cumulative_words = np.cumsum(daily_words)

page.ui.titles.subtitle("Plot Chart 1")

page.ui.titles.section("Formula")
page.ui.texts.formula(r'''$$ f(x) = \frac{2xe^{-x^ {\kern 0.04 em 2}/\alpha}}{\alpha} \qquad \qquad x > 0. $$''')

line = page.ui.charts.plot(chart_family, kind="line")
#line.labels(list(day_num))
line.add_dataset(daily_words, "daily")
line.add_dataset([float(i) for i in cumulative_words], "Cumulative daily")

code = page.ui.texts.code('''
line = page.ui.charts.plotly.line()
line.labels(list(day_num))
line.add_dataset(daily_words, "daily")
''')
page.ui.panels.sliding([code], "Python Code")


# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]
y2 = [2, 3, 4, 5, 6]
y3 = [4, 5, 5, 7, 2]

table = page.ui.table()

page.ui.titles.subtitle("Plot Chart 2")
lines = page.ui.charts.plot(chart_family, kind="line")
lines.colors(["blue", "red", "green", "orange", "purple"])
lines.labels(x)
lines.add_dataset(y, "test")
lines.add_dataset(y3, "test 3", kind="scatter")
lines.add_dataset(y2, "test 2", kind="line")
lines.shared.y_label("Y Axis")
lines.shared.x_label("X Axis")

code = page.ui.texts.code('''
lines = page.ui.charts.plot(chart_family, kind="line")
lines.colors(["blue", "red", "green", "orange", "purple"])
lines.labels(x)
lines.add_dataset(y, "test")
lines.add_dataset(y3, "test 3", kind="scatter")
lines.add_dataset(y2, "test 2", kind="line")
lines.shared.y_label("Y Axis")
lines.shared.x_label("X Axis")
''')
page.ui.panels.sliding([code], "Python Code")

#line.options.elements.line.tension = 0

rs = np.random.RandomState(365)
values = rs.randn(365, 4).cumsum(axis=0)
dates = pd.date_range("1 1 2016", periods=365, freq="D")
df = pd.DataFrame(values, dates, columns=["A", "B", "C", "D"])
df = df.rolling(7).mean()
df = df.reset_index()
df["index"] = df["index"].dt.strftime('%Y-%m-%d')

page.ui.titles.subtitle("Plot Chart 3")
scatter = page.ui.charts.plot(
  chart_family, df.to_dict(orient="records"), y=["A", "B", "C", "D"], x="index", kind="bar")


code = page.ui.texts.code('''
page.ui.titles.subtitle("Plot Chart 3")
scatter = page.ui.charts.plot(
  chart_family, df.to_dict(orient="records"), y=["A", "B", "C", "D"], x="index", kind="bar")
''')

page.ui.panels.sliding([code], "Python Code")


page.ui.titles.subtitle("Plot Chart 4")
df = pd.DataFrame(np.random.randn(500, 2).cumsum(axis=0), columns=["x", "y"])
line = page.ui.charts.plot(chart_family, df.to_dict(orient="records"), y=["y"], x="x")

code = page.ui.texts.code('''
line = page.ui.charts.plot(chart_family, df.to_dict(orient="records"), y=["y"], x="x")
''')

page.ui.panels.sliding([code], "Python Code")

page.ui.layouts.hr()
page.ui.titles.subtitle("Report powered by")
page.ui.rich.powered()

if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()
