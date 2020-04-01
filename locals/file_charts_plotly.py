
from epyk.core.Page import Report
from epyk.tests import data_urls

import config

# Create a basic report object
rptObj = Report()
rptObj.body.set_background()

data_series = config.getSeries(5, 30)

z1 = [[
    [8.83,8.89,8.81,8.87,8.9,8.87],
    [8.89,8.94,8.85,8.94,8.96,8.92],
    [8.84,8.9,8.82,8.92,8.93,8.91],
    [8.79,8.85,8.79,8.9,8.94,8.92],
    [8.79,8.88,8.81,8.9,8.95,8.92],
    [8.8,8.82,8.78,8.91,8.94,8.92],
    [8.75,8.78,8.77,8.91,8.95,8.92],
    [8.8,8.8,8.77,8.91,8.95,8.94],
    [8.74,8.81,8.76,8.93,8.98,8.99],
    [8.89,8.99,8.92,9.1,9.13,9.11],
    [8.97,8.97,8.91,9.09,9.11,9.11],
    [9.04,9.08,9.05,9.25,9.28,9.27],
    [9,9.01,9,9.2,9.23,9.2],
    [8.99,8.99,8.98,9.18,9.2,9.19],
    [8.93,8.97,8.97,9.18,9.2,9.18]
]]

# url_data = r'https://raw.githubusercontent.com/plotly/datasets/master/polar_dataset.csv'
# data_line_3d = r'https://raw.githubusercontent.com/plotly/datasets/master/3d-line1.csv'
# data_line_3d = r'https://raw.githubusercontent.com/plotly/datasets/master/_3d-line-plot.csv'
# data_line_3d = r'https://raw.githubusercontent.com/plotly/datasets/master/mesh_dataset.txt'

# data = rptObj.py.requests.csv(data_line_3d, delimiter=" ", with_header=False)



data = rptObj.py.requests.csv(data_urls.PLOTLY_WEBGL_POLAR, store_location=config.OUTPUT_TEMPS)

sc = rptObj.ui.charts.plotly.scatterpolar(data, r_columns=['trial_1_r'], theta_axis='trial_1_theta')
sc.layout.no_background()

sc = rptObj.ui.charts.plotly.scatter(data_series, y_columns=[1, 2], x_axis=0)
sc.layout.no_background()
sc.layout.no_grid()

shape = sc.layout.shapes.add_line(-100, 10, -50, -10, color="red")
an = sc.layout.annotations
an.text = "Super"
an.x = 10
an.y = 10
an.showarrow = False
an.font.color = 'red'

# shape = sc.layout.shapes.circle('2015-01-31', 1, '2016-01-01', 1)
# shape.type = 'rect'
# shape.xref = 'x'
# shape.yref = 'paper'
# shape.x0 = '2017-01-31'
# shape.y0 = 0
# shape.x1 = '2017-02-01'
# shape.y1 = 1
# shape.fillcolor = 'yellow'


s3d = rptObj.ui.charts.plotly.scatter3d(data, y_columns=["y1", "y2"], x_columns=["x1", "x2"], z_columns=["z1", "z2"])
s3d.data.opacity = 0.5
s3d.layout.grid_colors('white')
s3d.layout.axis_colors('white')
s3d.layout.no_background()


pie = rptObj.ui.charts.plotly.pie()
pie.data.values = [2, 3, 4, 4]
pie.data.type = "pie"
pie.data.textinfo = "label+percent"
pie.data.textposition = "outside"
pie.data.automargin = True
pie.data.labels = ["Wages", "Operating expenses", "Cost of sales", "Insurance"]
pie.layout.no_background()
pie.data.outsidetextfont.color = 'white'

line = rptObj.ui.charts.plotly.line()
line.data.x = [19097, 18601, 15595, 13546, 12026, 7434, 5419]
line.data.y = [43, 47, 56, 80, 86, 93, 80]
line.data.mode = 'markers'
line.data.type = 'scatter'
line.data.name = 'Latin America'
line.data.text = ['Chile', 'Argentina', 'Mexico', 'Venezuela', 'Venezuela', 'El Salvador', 'Bolivia']
line.layout.no_grid()
line.layout.no_background()


bar = rptObj.ui.charts.plotly.bar()
bar.layout.no_background()
bar.layout.grid_colors('grey')
bar.layout.axis_colors('white')
bar.data.x = ['giraffes', 'orangutans', 'monkeys']
bar.data.y = [12, 18, 29]
bar.data.name = 'LA Zoo'
bar.data.type = 'bar'
bar.layout.barmode = 'stack'



#pie.layout.plot_bgcolor = 'rgba(0,0,0,0)'

mp = rptObj.ui.charts.plotly.maps(z1)
mp.data.contours.z.show = True
mp.data.contours.z.usecolormap = True
mp.data.contours.z.project.z = True


# me = rptObj.ui.charts.plotly.mesh3d(data, intensity="x", x=1, y=2, z=3)

#

l = rptObj.ui.charts.plotly.line(data, y_columns=[1, 2, 3, 4], x_axis='x')
su = rptObj.ui.charts.plotly.ribbon(data, y_columns=[1, 4], x_axis='x', z_axis='z')
sur = rptObj.ui.charts.plotly.surface(data, y_columns=[1], x_axis='x', z_axis=2)
b = rptObj.ui.charts.plotly.bar(data, y_columns=[1, 2], x_axis='x')
b.add_trace({"x": [1, 3 , 4, 5], 'y': [12, 10, 11, 7]}, type="scatter")

hist = rptObj.ui.charts.plotly.histogram(data, x_columns=['y', 'z'])
h = rptObj.ui.charts.plotly.hbar(data, y_columns=[3, 4], x_axis='x')
s = rptObj.ui.charts.plotly.scatter(data, y_columns=[1, 2], x_axis='x')
a = rptObj.ui.charts.plotly.area(data, y_columns=[1, 2], x_axis='x')

bu = rptObj.ui.charts.plotly.bubble(data, y_columns=[1, 2], x_axis='x')
bu.layout.title = "Test"
bu.layout.showlegend = True

p1 = rptObj.ui.charts.plotly.pie(data, y_columns=[2], x_axis='g')
p1.data.hole = 0.4
p1.data.textposition = "inside"

p2 = rptObj.ui.charts.plotly.pie(data, y_columns=[1], x_axis='g')

s2 = rptObj.ui.charts.plotly.scatter(data, y_columns=[1, 2, 3, 4], x_axis='x')
s2.traces(1).axis_index(3)
s2.traces(2).axis_index(2)
s2.traces(3).axis_index(4)
s2.layout.sub_plot(2, 2)
s2.layout.title = "Test Subplots"

#
s3 = rptObj.ui.charts.plotly.scatter(data, y_columns=[1, 2], x_axis='x')
s3.traces(1).axis_index(2)
s3.layout.xaxis.domain = [0, 0.7]
s3.layout.xaxis2.domain = [0.8, 1]
s3.layout.yaxis2.anchor = 'x2'
s3.layout.title = "Test Subplots 2"

#
l1 = rptObj.ui.charts.plotly.line(data, y_columns=[2, 3, 4], x_axis='x')
l1.traces(1).axis_index(2)
l1.traces(1).type = 'bar'
l1.traces(2).axis_index(3)
l1.layout.inset_trace([0.8, 1], 2)
l1.layout.inset_trace([0.8, 1], 3, y_domain=[0.1, 0.3])
l1.layout.title = "Inset"

# me1 = rptObj.ui.charts.plotly.mesh3d(data, intensity="x", x=1, y=2, z=3)
# me1.layout.yaxis.tickfont.color = "#1f77b4"

delta = rptObj.ui.charts.plotly.number_with_delta(2009860)
delta.data.delta.reference = 400
delta.data.vmax = 400
delta.data.gauge.shape = "bullet"
delta.data.delta.valueformat = ".0f"
delta.data.domain([0, 0.5], [0, 0.5])
delta.data.add_title("<b style='color:red'>test</b>")
#
# delta = rptObj.ui.charts.plotly.gauge(2000)
# delta.data.gauge.axis.range = [0, 5000]
#
#
# ##rptObj.ui.charts.plotly.scatterpolar(data)
#
# series = [
#   {"t": '2013-10-04 22:23:00', 'y': 1, 'y2': 4},
#   {"t": '2013-11-04 22:23:00', 'y': 3, 'y2': 2},
#   {"t": '2013-12-04 22:23:00', 'y': 6, 'y2': 8},
# ]
#

data = rptObj.py.requests.csv(data_urls.PLOTLY_APPLE_PRICES, store_location=config.OUTPUT_TEMPS)
#
ts = rptObj.ui.charts.plotly.timeseries(data, y_columns=['AAPL.Open', 'AAPL.High', 'AAPL.Low'], x_axis="Date")
ts.layout.no_background()

# ts = rptObj.ui.charts.plotly.timeseries(series, y_columns=['y', 'y2'], x_axis="t")
# ts.layout.xaxis.type = "date"
# ts.layout.xaxis.range = ['2016-07-01', '2016-12-31']
# ts.layout.xaxis.rangeslider.range = ['2013-10-04', '2016-12-31']
# ts.layout.xaxis.rangeselector.month(3)
# ts.layout.xaxis.rangeselector.month(6)
# ts.layout.xaxis.rangeselector.year()
# ts.layout.xaxis.rangeselector.all()

# b = rptObj.ui.charts.plotly.group_box(data, y_columns=[1, 2], x_axis='g')
# b.data.boxmean = 'sd'
# b.data.whiskerwidth = 0.4
# b.layout.boxmode = 'group'
# b.layout.yaxis.zeroline = False

data_geo_path = 'https://raw.githubusercontent.com/plotly/datasets/master/2014_us_cities.csv'
data_meteo_usa_path = 'https://raw.githubusercontent.com/plotly/datasets/master/2015_06_30_precipitation.csv'
data_meteo_usa_path = 'https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv'


tb = rptObj.ui.tables.plotlys.table([], [], [])
tb.columns_color(["red", "green"])
tb.columns_font_color(["green", "red"])
tb.add_trace({"x": [1, 2, 3], "y": [2, 1, 5]}, type="scatter")
tb.add_trace({"x": [1, 2, 3], "y": [2, 1, 5]}, type="bar")
tb.add_trace({"x": [1, 2, 3], "y": [2, 1, 5]}, type="bar")
tb.traces(1).axis_index(2)
tb.traces(2).axis_index(3)
tb.traces(3).axis_index(4)
tb.traces(0).set_domain([0, 0.7], [0, 1])

tb.layout.inset_trace([0.8, 1], 2)
tb.layout.inset_trace([0.8, 1], 3, y_domain=[0.4, 0.7])
tb.layout.inset_trace([0.8, 1], 4, y_domain=[0, 0.3])

s = rptObj.ui.charts.plotly.scatter(data, y_columns=[1, 2], x_axis='x')
s.add_trace({"x": [1, 2, 3, 35], "y": [20, 10, 50, 45]}, type="bar")
s.traces(1).yaxis = "y2"
s.layout.yaxis2.side = 'right'
s.layout.yaxis2.overlaying = 'y'
#s.layout.legend.xanchor = 'right'
s.layout.legend.orientation = 'h'
s.layout.yaxis2.title = 'yaxis2 title'

#
csv = rptObj.js.d3.csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")

scatter = rptObj.ui.charts.plotly.scatter()

but = rptObj.ui.button("test")
print(but.dom.d3.append('table').attr("style", "margin-left: 250px"))

but.click([
  scatter.dom.add_trace(x=csv.unpack("myDate", "Date"), y=csv.unpack("High", "AAPL.High")),
  scatter.dom.add_trace(x=csv.unpack("myDate", "Date"), y=csv.unpack("Open", "AAPL.Open")),
])

# rptObj.ui.button("delete").click([
#   scatter.dom.deleteTraces(0)
# ])
#
# columns = ["A", "B", 'C']
# data = [["1", 12, 23], ["2", 30, 45], ["2", 33, 92]]
#
# print( rptObj.body.dom.d3.var('svg').rappend("path").attr("class", "line").attr("d", rptObj.js.d3.svg.line().x().y()).toStr() )
#
# rptObj.js.addOnLoad([
#   csv,
#   rptObj.body.dom.d3.append('svg'),
#   #rptObj.body.dom.d3.var('svg').rappend("path").attr("class", "line").attr("d", rptObj.js.d3.svg.line().x().y()),
#
#   # Table creation from D3
#   rptObj.body.dom.d3.append('table').attr("style", "margin-left: 250px"),
#   rptObj.body.dom.d3.var('table').append("thead"),
#   rptObj.body.dom.d3.var('thead').rappend("tr").selectAll("th").data(columns).enter().rappend("th").text("test"),
#   rptObj.body.dom.d3.var('table').append("tbody"),
#   rptObj.body.dom.d3.var('tbody').selectAll("tr").data(data).enter().append("tr"),
#   rptObj.body.dom.d3.var('tr').selectAll("td").dataFncRows(columns).enter().rappend("td").html("")
# ])

l1 = rptObj.ui.charts.plotly.line(data, y_columns=[2, 3, 4], x_axis='x')
l1.layout.yaxis.set_color("#1f77b4")
l1.layout.xaxis.set_color("red")
l1.layout.yaxis.title = "Test"

rptObj.ui.grid([
  #[d, gs, me],
  [l, b, s, p1, sur],
  [bu, a, p2, h, hist]
])

print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_charts_plotly"))
