
import epyk as pk


# Create a basic report object
page = pk.Page()
page.headers.dev()

scripts = ["https://cdnjs.cloudflare.com/ajax/libs/venn.js/0.2.20/venn.min.js"]

data = [
  {'sets':["Audio"], 'figure': 27.92, 'label': "Audio", 'size': 27.92},
  {'sets':["Direct Buy"], 'figure': 55.28, 'label': "Direct Buy", 'size': 55.28},
  {'sets':["Branded Takeover"], 'figure': 7.62, 'label': "Branded Takeover", 'size': 7.62},
  {'sets': ["Audio", "Direct Buy"], 'figure': 3.03, 'label': "Audio and Direct Buy", 'size': 3.03},
  {'sets': ["Audio", "Branded Takeover"], 'figure': 1.66, 'label': "Audio and Branded Takeover", 'size': 1.66},
  {'sets': ["Direct Buy", "Branded Takeover"], 'figure': 2.40, 'label': "Direct Buy and Branded Takeover", 'size': 2.40},
  {'sets': ["Audio", "Direct Buy", "Branded Takeover"], 'figure': 1.08, 'label': "Audio, Direct Buy, and Branded Takeover", 'size': 1.08}
  ];

chart = page.ui.charts.d3.script('venn', scripts, data, dependencies=['d3-selection'])
chart.loader('''
var chart = venn.VennDiagram().width(500).height(400);

var div2 = htmlObj.datum(data).call(chart); div2.selectAll("text").style("fill", "white");
div2.selectAll(".venn-circle path").style("fill-opacity", .8).style("stroke-width", 1).style("stroke-opacity", 1).style("stroke", "fff");

var tooltip = d3.select("body").append("div").attr("class", "venntooltip");

div2.selectAll("g").on("mouseover", function(d, i) {

venn.sortAreas(div2, d);

tooltip.transition().duration(40).style("opacity", 1);
tooltip.text(d.size + "% of Audience Two saw " + d.label);

var selection = d3.select(this).transition("tooltip").duration(400);
selection.select("path").style("stroke-width", 3).style("fill-opacity", d.sets.length == 1 ? .8 : 0).style("stroke-opacity", 1);})
  .on("mousemove", function() {
  tooltip.style("left", (d3.event.pageX) + "px").style("top", (d3.event.pageY - 28) + "px");})

 .on("mouseout", function(d, i) {
      tooltip.transition().duration(2500).style("opacity", 0);
      var selection = d3.select(this).transition("tooltip").duration(400);
      selection.select("path").style("stroke-width", 3).style("fill-opacity", d.sets.length == 1 ? .8 : 0).style("stroke-opacity", 1);
  });
''')

