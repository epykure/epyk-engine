"""
Module in charge of the testing of the buttons
"""

import epyk as pk

from epyk.core.css import Defaults as css_defaults
from epyk.core.html import Defaults as html_defaults

#css_defaults.Font.size = 20
css_defaults.Font.family = "cursive"

html_defaults.SERVER_PATH = ""

# Create a basic report object
page = pk.Page()

# This line will never be sent to the Javascript as not in any container or dedicated Js function
# page.js.alert("Display")
#
# page.js.addOnReady([
#   page.js.console.log("This is a Javascript Log"),
#   page.js.console.log(page.js.location.pathname),
#   page.js.console.log(page.js.math.log(2)),
#   page.js.localStorage.setItem("A", 30),
#   page.js.console.log(page.js.localStorage["A"])
# ])
#
# # Create a variable
# page.js.addOnReady([
#   page.js.objects.number(344, varName="test_number", setVar=True),
#   page.js.objects.number.get("test_number") + 5,
#   page.js.console.log(page.js.objects.number.get("test_number")),
#
#   #
#   page.js.fncs.inline("MyFncs", [page.js.alert(page.js.objects.get("a"))], ["a"]),
#   page.js.fncs.get("MyFncs", "test call")
# ])


# Create a Javascript function

#button = page.ui.button("test")
# # button.style.clear()
#
# # Create a new CSS class on the fly dedicated to the small devices
# button.style.cssCls("test", {"background-color": 'yellow'}, isMedia=True)
# # Derive from an existing CSS class
# button.defined.ovr("CssButtonBasic", eventAttrs={'hover': {"cursor": "cell"}})
# button.click(page.js.window.alert("test"))

# Change the style for the CSS HTML Title component
# title = page.ui.title("Example of title", level=1)
# title.style.cssCls("title_style", {"color": 'orange'})

# title.style.clear()

# Change the style for the CSS HTML Text component
# text = page.ui.text("This is a text")
# text.style.clear().cssCls("class_text", {"color": 'red'}, {"hover": {"color": 'green', "cursor": "all-scroll"}})
# text.tooltip("This is a tooltip")
#
# page.ui.input()
# page.ui.css({"border": "1px solid red"})

# Javascript tests

data = [{"A": 1, "B": 2}]
table = page.ui.tables.tabulators.table(data, cols=["A"], rows=["B"])
table.on("dblclick", page.js.alert("test"), profile=False)

button = page.ui.button("Test") # .click(page.js.alert("test"))
page.ui.rich.info("info")
span = page.ui.texts.span("youpi")
span.mouse([
  span.dom.css("color", "red"),
  span.dom.css("cursor", "pointer").r],
  span.dom.css("color", "blue").r)

#span.on("mouseover", span.dom.css("color", "red"))
#span.on("mouseleave", span.dom.css("color", "blue"))

label = page.ui.texts.label("label")

pre = page.ui.texts.preformat("Super").selectable(False)

#page.ui.media.youtube("https://www.youtube.com/embed/dfiHMtih5Ac")
data = [
  {"test": 'A', 'value': 10},
]

label = page.ui.texts.label("test label").css({"display": 'block'}, reset=True).selectable(False)
page.ui.layouts.new_line()
text = page.ui.text("this is a **test**", options={'maxlength': 2})

fieldset = page.ui.texts.fieldset('legend')
fieldset.add_label("Label")
fieldset.add_title("title")

highlights = page.ui.texts.highlights("Test content", title="Test", icon="fab fa-angellist")

paragraph = page.ui.texts.paragraph("\n".join([
  "This is a paragraph",
  "This is a second line"
]))

input = page.ui.inputs.input("test input")
input.autocomplete(["AAAAA", "AAABBB"])
input.focus(options={"reset": True})


input_color = page.ui.inputs.input("Capture.PNG")

img = page.ui.images.img("philo.PNG")
page.ui.images.badge("new", "Label", icon="fas fa-align-center").css({"border": '1px solid red'})

emoji = page.ui.images.emoji(page.entities.html5_c.cap)

button.click([
  input.build("data", {"css": {"backgroundColor": input_color.dom.val[input_color.htmlCode]['value']}}),
  input.dom.empty(),
  highlights.title.build(input_color.dom.val[input_color.htmlCode]['value']),
  highlights.icon.build("fas fa-adjust"),
  img.build({"image": input_color.dom.content}), # 'Capture.PNG'
  page.js.console.log(highlights.icon.dom.val),
  fieldset.build("ok"),
  emoji.build(page.entities.html4.APL_OVERBAR),
  text.build(input_color.dom.val[input_color.htmlCode]['value'],
             {"reset": True, 'css': {"backgroundColor": 'yellow'}})
], profile=True)
# page.ui.texts.paragraph("This is a paragraph", helper="Paragraph helper")

progress_bar = page.ui.sliders.progressbar(30)
pre.click([
  page.js.console.log(pre.dom.val),
  page.js.console.log(span.dom.val),
  page.js.console.log(label.dom.val),
  progress_bar.build(50)
])

# print( progress_bar.dom.val )
from datetime import datetime

timestamp_s = page.py.dates.from_timestamp(1573074335010, 0)

#from epyk.mocks.add_ons import EntAddOn
#html_defaults.ENTITIES_ADD_ON = EntAddOn


