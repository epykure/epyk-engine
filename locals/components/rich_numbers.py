
from epyk.core.Page import Report


page = Report()
page.headers.dev()

# Console component
c = page.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

#
n = page.ui.numbers.digits(76862.095)
n.style.color = "red"


n1 = page.ui.text(76862.095)

#
delta = page.ui.charts.plotly.number_with_delta(2009860)
delta.data.delta.reference = 400
delta.data.vmax = 400
delta.data.gauge.shape = "bullet"
delta.data.delta.valueformat = ".0f"
delta.data.domain([0, 0.5], [0, 0.5])
delta.data.add_title("<b style='color:red'>test</b>")

# Change the number of digit on the component loading
n1.onReady([
  n1.dom.format.number.toFixed(6)
])

# Display logs on click
page.ui.button("display").click([
  page.js.alert(n1.dom.content.number.toFixed(5)),
  c.dom.write(n1.dom.val, stringify=True, format="Number: %s")
])

# Change the value displayed and the format
page.ui.button("click").click([
  n1.build(-38866),
  n1.dom.format.toMoney('£')
])

c.move()

