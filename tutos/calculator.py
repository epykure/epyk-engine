from epyk.core.Page import Report
from epyk.core.css.themes import ThemeBlue


page = Report()
page.headers.dev() # Change the Epyk logo
page.theme = ThemeBlue.BlueGrey()
page.body.template.style.configs.doc(background="white")

input = page.ui.inputs.left()
buttons = []
for i in range(1, 10):
  buttons.append(page.ui.button(str(i)))
  buttons[-1].click([input.build(buttons[-1].dom.content)])

grid = page.ui.layouts.columns(buttons, 3, width=(200, 'px'))
grid.style.css.padding = "10px 20px 10px 0"

plus = page.ui.button("+")
clear = page.ui.button("Clear")
clear.click(input.build(""))
enter = page.ui.button("Enter")

# Pure JavaScript
input2 = page.ui.input(placeholder="Enter an expression")
input2.enter([input2.build(page.js.eval(input2.dom.content))])

display = page.ui.button("Add")
clearSeries = page.ui.button("Clear")

input3 = page.ui.input(10)
input4 = page.ui.input(-10)

line = page.ui.charts.chartJs.line(y_columns=["y"], x_axis="x")
line.options.elements.point.radius = 0

clearSeries.click([line.build([])])

display.click([
  # for look on the JavaScript
  page.js.objects.array.new([], varName="myArray"),
  page.js.for_([
    page.js.objects.array.get("myArray").push_dict(
      x=page.js.objects.number.get("i"), y=page.js.objects.function(["i"], input2.dom.content.toStr(), eval=True)),
  ], start=input4.dom.content,  end=input3.dom.content),
  line.build(page.js.objects.array.get("myArray"))
])

container = page.ui.div()
container.extend([input, grid, plus, clear, enter, input2, display, clearSeries, input3, input4, line])
container.style.standard()


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()


