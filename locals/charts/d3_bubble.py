
import epyk as pk


# Create a basic report object
page = pk.Page()
page.headers.dev()

data = [
  {'x': 200, "y": 10, 'size': 50, 'radius': 5},
  {'x': 200, "y": 10, 'size': 50, 'radius': 15},
  {'x': 20, "y": 100, 'size': 500, 'radius': 50},
]

chart = page.ui.charts.d3.script('bubble', data=data)
chart.loader('''
  const width = 940;
  const height = 500;
  
  // location to centre the bubbles
  const centre = { x: width/2, y: height/2 };

  // strength to apply to the position forces
  const forceStrength = 0.03;

  // these will be set in createNodes and chart functions
  let svg = null;
  let bubbles = null;
  let labels = null;
  let nodes = [];
  
  function charge(d) {
    return Math.pow(d.radius, 2.0) * 0.01
  }
  
  const fillColour = d3.scaleOrdinal()
  	.domain(["1", "2", "3", "5", "99"])
  	.range(["#0074D9", "#7FDBFF", "#39CCCC", "#3D9970", "#AAAAAA"]);

  const simulation = d3.forceSimulation()
    .force('charge', d3.forceManyBody().strength(charge))
    // .force('center', d3.forceCenter(centre.x, centre.y))
    .force('x', d3.forceX().strength(forceStrength).x(centre.x))
    .force('y', d3.forceY().strength(forceStrength).y(centre.y))
    .force('collision', d3.forceCollide().radius(d => d.radius + 1));

  function ticked() {
    bubbles
      .attr('cx', d => d.x)
      .attr('cy', d => d.y)

    labels
      .attr('x', d => d.x)
      .attr('y', d => d.y)
  };
  
  nodes = data;

  svg = htmlObj
    .append('svg')
    .attr('width', width)
    .attr('height', height)

  const elements = svg.selectAll('.bubble')
    .data(nodes, d => d.id)
    .enter()
    .append('g')

  bubbles = elements
    .append('circle')
    .classed('bubble', true)
    .attr('r', d => d.radius)
    .attr('fill', d => fillColour(d.groupid))

  labels = elements
    .append('text')
    .attr('dy', '.3em')
    .style('text-anchor', 'middle')
    .style('font-size', 10)
    .text(d => d.id)

  simulation.nodes(nodes)
    .on('tick', ticked)
    .restart();
''')

