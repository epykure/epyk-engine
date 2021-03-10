from epyk.core.Page import Report
from epyk.core.css.themes import ThemeBlue
from epyk.tests import data_urls
from epyk.core.js import std
from epyk.core.data import datamap


page = Report()
page.theme = ThemeBlue.BlueGrey()

world = page.ui.geo.chartJs.choropleths.world(height=200)
world.plugins.datalabels.display = False
world2 = page.ui.geo.chartJs.choropleths.world(height=200)
world2.plugins.datalabels.display = False

title = page.ui.title("COVID Map")
title_country = page.ui.title()
title_country2 = page.ui.title()

bar = page.ui.charts.chartJs.bar([], ['Confirmed', 'Deaths', 'Recovered'], 'Country/Region', height=200)
bar.options.scales.y_axis().ticks.toNumber()
bar.options.tooltips.callbacks.labelNumber()
bar.plugins.datalabels.formatters.details()
bar.options.legend.display = False

bar2 = page.ui.charts.chartJs.bar([], ['Confirmed', 'Deaths', 'Recovered'], 'Country/Region', height=200)
bar2.options.scales.y_axis().ticks.toNumber()
bar2.options.tooltips.callbacks.labelNumber()
bar2.plugins.datalabels.formatters.details()
bar2.options.legend.display = False

row = page.ui.row([world, [title_country, bar]], position="top")
row.set_size_cols(7)
row.options.responsive = False

row2 = page.ui.row([world2, [title_country2, bar2]], position="top")
row2.set_size_cols(7)
row2.options.responsive = False

powered = page.ui.rich.powered()
ref = page.ui.texts.references.website(author="rsharankumar", name="Learn Data Science in 100Days", site="github",
                                       url="https://github.com/rsharankumar/Learn_Data_Science_in_100Days")

# Create a container for the HTML page
box = page.ui.div()
box.extend([title, powered, row, row2, ref])
box.style.doc()

# Group data for the processing on the JavaScript side
grp = page.data.js.record(std.var("covidData", global_scope=True)).filterGroup("aggData")
grp3 = page.data.js.record(std.var("covidData", global_scope=True)).filterGroup("aggData3")
grp2 = page.data.js.record(std.var("covidData", global_scope=True)).filterGroup("aggData2")

world.click([
  page.js.if_(world.activePoints().label == "United States of America", [
    title_country.build("US"),
    bar.build(grp.match(datamap(attrs={"Country/Region": "US"})).group().sumBy(
      ["Deaths", 'Confirmed', 'Recovered'], ["Country/Region"], cast_vals=True))
  ]).else_([
    title_country.build(world.activePoints().label),
    bar.build(grp3.match(datamap(attrs={"Country/Region": world.activePoints().label})).group().sumBy(
      ["Deaths", 'Confirmed', 'Recovered'], ["Country/Region"], cast_vals=True))
  ])
])

world2.click([
  page.js.if_(world2.activePoints().label == "United States of America", [
    title_country2.build("US"),
    bar2.build(grp.match(datamap(attrs={"Country/Region": "US"})).group().sumBy(
      ["Deaths", 'Confirmed', 'Recovered'], ["Country/Region"], cast_vals=True))
  ]).else_([
    title_country2.build(world2.activePoints().label),
    bar2.build(grp3.match(datamap(attrs={"Country/Region": world2.activePoints().label})).group().sumBy(
      ["Deaths", 'Confirmed', 'Recovered'], ["Country/Region"], cast_vals=True))
  ])
])


page.body.onReady([
  std.var("covidData", value=[], global_scope=True),
  page.js.d3.csv(data_urls.COUNTRY_WISE_COVID).records(std.var("covidData", global_scope=True)).then([
    world.build(grp2.group().sumBy(["Deaths"], ["Country/Region"], cast_vals=True).to_dict('Country/Region', 'Deaths')),
    world2.build(grp2.group().sumBy(["Deaths"], ["Country/Region"], cast_vals=True).to_dict('Country/Region', 'Deaths')),
  ])
])