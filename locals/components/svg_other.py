
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

poly = page.ui.charts.svg.rectangle(50, 50, 50, 50, rx=20, ry=20)
poly[0].transform("transform", "rotate", "0 100 100", "360 100 100")
poly.css({"margin": '10px', "border": "1px solid black"})

poly.text("Ok", 50, 50)
poly[-1].transform("transform", "rotate", "0 100 100", "360 100 100")
poly[-1].line("New line", 50, 60)

defs = poly.defs()
gradients = defs.radialGradient("gradient_test")
gradients.stop("20%", {"stop-color": "pink", "stop-opacity": 1})
gradients.stop("95%", {"stop-color": "green", "stop-opacity": 1})
m = defs.marker("arrow", "0 0 10 10", 5, 5)
m.circle(5, 5, 5, 'red')
ma = defs.marker("arrow_arrow", "0 0 10 10", 5, 5)
ma.arrow()
ma.markerWidth(10).markerHeight(10)

poly.line(1, 20, 20, 30)
pl = poly.polyline([(15, 80), (29, 50), (43, 60), (57, 30), (71, 40), (85, 15)])
pl.markers(ma.url)


poly[0].fill(gradients.url)

poly.circle(20, 50, 3, fill=gradients.url)
poly.ellipse(20, 40, 10, 20)
poly.polygon([(20, 60), (40, 19), (16, 19), (100, 100)], fill=gradients.url) # .css({"fill": gradients.url})
g = poly.g()
f = poly.foreignObject(10, 20, "100%", 150)
f.add([
    page.ui.texts.label("Test Label").css({"color": 'red'}),
    page.ui.input()
])

g.css({"stroke": 'blue'})
