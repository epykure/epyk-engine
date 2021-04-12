
from epyk.core.Page import Report

page = Report()
template = page.body.add_template(defined_style="doc")
template.style.css.background = "white"

value1 = page.ui.fields.number(label="Value 1", options={"scroll": False})
value2 = page.ui.fields.number(label="Value 2")
result = page.ui.fields.text("&nbsp;", label="Result", tooltip="Result")
result.style.css.border = "1px solid red"
result.style.css.padding = 5
result.style.css.min_width = 50

page.ui.button("Sum", align="center").click([
  result.input.build(value1.dom.content.number + value2.dom.content.number)
])
