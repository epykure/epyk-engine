from epyk_studio.core.Page import Report
from epyk.core.css.themes import ThemeBlue
from epyk.tests import data_urls
from epyk.core.js import std
from epyk.core.data import datamap



page = Report()
page.theme = ThemeBlue.BlueGrey()

dt = page.ui.fields.date(value=None, html_code="date", label="Date")

us = page.ui.geo.chartJs.choropleths.us()

#world = page.ui.geo.chartJs.choropleths.world()
#world.click([
#  page.js.console.log(world.activePoints().label)
#])

#france = page.ui.geo.chartJs.choropleths.country()


bar_total = page.ui.charts.chartJs.bar(y_columns=["cases", "deaths", "fips"], x_axis="state")
bar_total.options.scales.y_axis().ticks.toNumber()
bar_total.options.tooltips.callbacks.labelNumber()
bar_total.options.stacked = True

title_county = page.ui.title("View per counties")
bar = page.ui.charts.chartJs.bar(y_columns=["cases", "deaths"], x_axis="county")
bar.options.scales.y_axis().ticks.toNumber()
bar.options.stacked = True
bar.options.tooltips.callbacks.labelNumber()

row = page.ui.row([bar, bar_total])
row.set_size_cols(9)

title_state = page.ui.title()
line_cumul = page.ui.charts.chartJs.line(y_columns=["cases", "deaths"], x_axis="date")
line_cumul.options.scales.y_axis().ticks.toNumber()
line_cumul.options.stacked = True
line_cumul.options.tooltips.callbacks.labelNumber()

title = page.ui.title()
line_cumul_county = page.ui.charts.chartJs.line(y_columns=["cases", "deaths"], x_axis="date")
line_cumul_county.options.scales.y_axis().ticks.toNumber()
line_cumul_county.options.stacked = True
line_cumul_county.options.tooltips.callbacks.labelNumber()

# Create a container for the HTML page
box = page.studio.containers.box()
box.extend([dt, page.ui.row([us, [title_state, line_cumul]]), title_county, row, title, line_cumul_county])
box.style.standard()

# Group data for the processing on the JavaScript side
grp = page.data.js.record(std.var("covidData", global_scope=True)).filterGroup("aggData")
grp2 = page.data.js.record(std.var("covidData", global_scope=True)).filterGroup("aggData2")
grp3 = page.data.js.record(std.var("covidData", global_scope=True)).filterGroup("aggData3")
grp4 = page.data.js.record(std.var("covidData", global_scope=True)).filterGroup("aggData4")
grp5 = page.data.js.record(std.var("covidData", global_scope=True)).filterGroup("aggData5")

# Events sections for the interactivity
dt.select(
  us.build(grp.match(datamap(components=[dt])).group().sumBy(["deaths"], ["state"], cast_vals=True).to_dict('state', 'deaths') )
)

us.click([
  title_state.build(us.activePoints().label),
  bar.build(grp.match(datamap(attrs={"state": us.activePoints().label}, components=[dt])).group().sumBy(["cases", "deaths"], ["county"], cast_vals=True)),
  bar_total.build(grp4.match(datamap(attrs={"state": us.activePoints().label}, components=[dt])).group().sumBy(["cases", "deaths", "fips"], ["state"], cast_vals=True)),
  line_cumul.build(grp2.match(datamap(attrs={"state": us.activePoints().label})).group().sumBy(["cases", "deaths"], ["date"], cast_vals=True)),
  line_cumul_county.build([]),
  title.build(""),
])

bar.click([
  title.build(bar.activePoints().label),
  line_cumul_county.build(grp3.match(datamap(attrs={"state": title_state.dom.content, "county": bar.activePoints().label})).group().sumBy(["cases", "deaths"], ["date"], cast_vals=True)),
])


page.body.onReady([
  std.var("covidData", value=[], global_scope=True),
  page.js.d3.csv(data_urls.COVID_US).records(std.var("covidData", global_scope=True))
])