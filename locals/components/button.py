
from epyk.core.Page import Report
from epyk.core.data import components

from epyk.core.js.packages import JsFontAwesome


# Defaults_css.Font.size = 20
# Create a basic report object
page = Report()
page.headers.dev()

page.ui.components_skin = {
  "buttons.absolute": {"clear": {"css": True, "cls": True}, "css": {"color": "red"}, 'cls': ["cssbuttonbasic"]},
  "buttons.check": {"css": {"color": "green"}},
}

page.ui.buttons.absolute("Click Me")
# page.ui.lists.list(["A", "B"])

#g = page.ui.layouts.grid([t, t2, t3])

#page.ui.button('toggle').click([
  #g.dom.panels, #.css("border", "1px solid black"),
#  g.dom.panel(3).toggle() # .css("border", "1px solid black")
#])


#ts = [page.ui.text("test %s" % i) for i in range(5)]
#ts2 = [page.ui.text("test %s" % i).css({"border": "1px solid black"}) for i in range(2)]
# tab = page.ui.panels.tabs()
# for i in range(5):
#   tab.add_panel("Panel %s" % i, page.ui.text("test %s" % i))
# #
# #
# sw = page.ui.button("Ok")
# d = page.ui.div().css({"border": "1px solid black"})

#t1 = page.ui.text()
#t1.style.css.color = "green"
#t1.inReport = False
# htmlCode
# sw.click([
#   tab.dom.tab(3).firstChild.css({"color": 'red'}),
#   #tab.dom.add_tab("test"),,
#   #page.js.objects.new(str(t1), isPyData=True, varName="obj"),
#   #d.dom.loadHtml(page.js.objects.get("obj")),
#   #page.js.console.debugger,
#   d.dom.loadHtml([
#     page.ui.icon("fab fa-python"),
#     page.ui.layouts.new_line()
#   ], append=True),
#   #t1.build("ok")
# ])

import random

cols, row = 10, 30
rec = []
for i in range(row):
  row = {}
  for j in range(cols):
    row["col_%s" % j] = random.randint(1, 100)
  rec.append(row)

simple_table = page.ui.tables.grid(rec, cols=["col_%s" % i for i in range(int(cols/2))],
                                     rows=["col_%s" % i for i in range(int(cols/2), cols)])
# simple_table.add({"COL1": "Value", 'COL2': 'Field'})

#poly.animate("transform", "rotate", "0 190 50", "360 190 50")

#
# sw = page.ui.buttons.switch({'on': "true", 'off': 'false'})
# sw.click([
#   page.js.console.log(sw.content),
#   sw.dom.set_text("ok"),
# ])
# page.ui.rich.update("Last update: ")
# cd = page.ui.rich.countdown("2050-09-24")
# pre = page.ui.texts.preformat("This is a pre formatted text")
# pre.style.css.border = "1px solid black"
# inp = page.ui.input("")
#
# page.ui.button("TEst").click([
#   page.js.console.log(inp.dom.content),
#   pre.dom.append(inp.dom.content, new_line=True),
# ])
#
# d = page.ui.div()
# d.style.css.width = 200
# d.style.css.height = 1200
# d.style.css.border = "1px solid black"
#
# i = page.ui.images.icon(JsFontAwesome.ICON_ENVELOPE)
# c = page.ui.texts.text("test glow")
# c.style.effects.glow("pink")
#
# d1 = page.ui.div([i, c])
#
# b = page.ui.texts.text("test blink")
# b.style.effects.blink()
#
# st = page.ui.rich.stars(3, label="test", helper="This is a helper")
# st.click([
#   page.js.console.log("data", skip_data_convert=True),
#   page.js.navigator.geolocation.watchPosition("alert", "test")
# ])
#
#
# inp = page.ui.input()
#
# ch = page.ui.buttons.check(label="Label")
# ch.click(
#   ch.label.build(inp.dom.content)
# )
#
# page.ui.buttons.mail().color("blue")
#
# page.ui.buttons.check(True, label="Label")
# page.ui.buttons.check(True, label="Label", icon="fas fa-align-center")

# c = page.ui.div("ok")
#
# c.style.css.width = 100
# c.style.css.font_size = 80
# c.style.css.background_color = "white"
# c.style.css.height = 100
# c.style.css.color = 'yellow'
# # c.style.css.border = "1px solid black"
# c.style.css.border_radius = 100
# c.style.css.middle()
#
# c.style.css.shadow_box()
# c.style.css.shadow_text()

#c.style.css.sticky()
# c.style.effects.animate("pink", {"color": "blue", "width": "400px"})

#d += d1

# sw.style.css_class.keyframes("test", {
#   "50%": {"transform": "scale(1.5, 1.5)", "opacity": 0},
#   "99%": {"transform": "scale(0.001, 0.001)", "opacity": 0},
#   "100%": {"transform": "scale(0.001, 0.001)", "opacity": 1},
# })
#
# page.ui.button("Ok").style.css_class.animation('test', {
#   "from": {"border-color": "white"},
#   "to": {"border-color": "red"},
# })

# ps += ts2


# for i in range(3):
#   ps += page.ui.layouts.col([
#     page.ui.text("test %s" % i),
#     page.ui.text("test %s" % (i+1))])


#ps[1].css({"border": "1px solid black"})

#ps = page.ui.layouts.row(ts)
#ps[1].css({"color": 'red'})

#page.ui.button("Test").click([
#  ts[0].build("ok")
#])

#page.ui.buttons.zipfile("This is the data", "filename.txt")

# ps.title.style.css.color = "red"
#
# page.ui.input("test")
# number = page.ui.vignets.number(500, "Test")
#
# page.ui.icons.github()
# page.ui.icons.python()
# f = page.ui.icons.facebook()
# i = page.ui.icons.epyk()

# page.ui.layouts.iframe("http://www.google.com")
#
# page.ui.inputs.input()
#
# page.ui.fields.input(label="test")
# page.ui.fields.now(label="Time field")
# page.ui.fields.cob(label="COB Date")
# page.ui.fields.today(label="Date").selectable(["2019-09-01", "2019-09-06"])
# page.ui.fields.textarea(label="Date")
# page.ui.fields.password(label="password")
#
# page.ui.slider(recordSet=[1, 2, 3, 4, 5, 6, 7])
#
# div = page.ui.div([])
#
# b = page.ui.button("add")
# b.click([
#   page.js.alert(page.js.navigator.language),
#   div.dom.jquery.load(r"./report_list.html")
# ])
#
#
# page.ui.navigation.pin()
#
# page.ui.buttons.switch()
# page.ui.buttons.radio([{'value': 'test'}])
#
# page.ui.texts.code("This is a code")
#
# page.js.customFile("test.js")
#
# page.ui.rich.delta({'number': 100, 'prevNumber': 60, 'thresold1': 100, 'thresold2': 50}, helper="test")
#
# page.ui.navigation.indices(10)
#
# menu = page.ui.layouts.icons(["fas fa-bell", "fas fa-calendar-check"])
# menu[0].click([menu[0].dom.css({"color": 'red'})])
#
#
# p = page.ui.navigation.points(10)
# for i, _ in enumerate(p):
#   p.click(i, [])
#
# e = page.ui.links.external('data', 'www.google.fr', icon="fas fa-align-center", options={"target": "_blank"})
# e.no_decoration
#
# data_link = page.ui.links.data("link", "test#data")
# data_link.build({"text": 'new link Name', 'data': "new content"})
#
# b = page.ui.button("Test")
# page.ui.navigation.dots(10)
# page.ui.navigation.points(10)
#b.options.multiple

#page.ui.media.youtube("https://www.youtube.com/embed/dfiHMtih5Ac")

#page.ui.sliders.progressbar(50)

#page.ui.info("Test")
#page.ui.rich.stars(3, label="test", helper="This is a helper")

#e = page.ui.images.emoji(page.symbols.smileys.DISAPPOINTED_FACE)
#e.style.css.font_size = 30
#print(e.style.css.attrs)

# records = [
#       {"label": 'python', 'value': 12},
#       {"label": 'Java', 'value': 5},
#       {"label": 'Javascript', 'value': 80}]
# page.ui.charts.skillbars(records, y_column=['value'], x_axis=['label']).css({"width": '100px'})
#
# i = page.ui.images.icon("fab fa-angellist")
# i.click(page.js.alert(""))
#
# page.ui.buttons.badge("test", 10, options={"badge_css": {"color": "white", "background-color": "red"},
#                         "badge_position": 'left'})
#
#
# b = page.ui.button("test")
# print(b.style.classList)
# print(b.style.get_classes())

# d = page.ui.div("Test")
# print(d.style.get_classes())

# p = page.ui.layouts.panel([d])
#page.style.add_classes.button.success()

#button = page.ui.button("test")
#button.style.add_classes.external("youpi")
#button.style.add_classes.input.is_valid()
#success = button.style.define_classes.button.success()

#button.click(page.js.alert(''))

#
# # Console component
# page.ui.icons.facebook()
# page.ui.icons.twitter()
# page.ui.icons.linkedIn()
# page.ui.icons.youtube()
#
# c = page.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})
#
# i = page.ui.icon("fas fa-bolt")
# div = page.ui.div([i], width=(20, 'px')).css({"border": "1px solid black", "text-align": "center"})
# div.style.css_border_radius = "20px"
# div.style.css_background_color = "pink"
#
# div.style.animation(EffectsMoves.EffectsTranslate(), duration=3, timing_fnc="ease-out")
#
# b = page.ui.button("test")
#
# # Simple button
#
# b.click([
#   page.js.jquery.ajax("POST", 'https://jsonplaceholder.typicode.com/posts/1',
#                         successFncs=[
#                           b.build(page.js.objects.result["title"]),
#                           "console.log(result)"]),
#   c.write(" **ok**, this is a test")])
#
# # Press Button
# b2 = page.ui.button("test 2", width=100)
# b2.press(c.write(b2.dom.content + "' is locked'"))
#
#
# # Press Button and unlock
# b3 = page.ui.button("test 3", width=100)
# b3.press(
#   c.write("Button 3 locked", timestamp=False),
#   c.write("Button 3 unlocked"))
#
# # Create a group of buttons
# b5 = page.ui.button("test 5")
# b6 = page.ui.button("test 6")
# b7 = page.ui.button("test 7")
#
# # Change button CSS classes
# b8 = page.ui.button("test 8")
# b8.style.clear() # Remove all CSS classes
# b8.css({"background-color": 'blue', 'color': 'white', 'border': 'None'})
#
# page.ui.layouts.hr()
# # Create a CSS class
# b8_bis = page.ui.button("test CSS Class")
# b8_bis.style.clear()
# css_cls = page.style.cssCls("test_css", {"color": "orange"}, {"hover": {"color": 'red'}})
# b8_bis.style.cssCls("test_css")
#
# page.ui.layouts.new_line(1)
# # Change button hover CSS style
# b9 = page.ui.button("test 9")
# b9.color("red")
#
# # Button middle page
# b10 = page.ui.button("test 10")
# page.ui.div(b10).css({"text-align": 'center'})
#
# # Create a button with an icon
# b11 = page.ui.button("test 11", icon="fab fa-python")
#
# # Buttons categories
#b12 = page.ui.lists.buttons(["test 15", "test 13", "test 14"])
# for i in b12:
#   i.press(
#     page.js.console.log("test"),
#     [page.js.console.log("unlock")])
#
# # Buttons categories (manual)
# b15 = page.ui.button("test 15", options={"group": "test_group"})
# b16 = page.ui.button("test 16", options={"group": "test_group"})
# b15.options.multiple = True
# b16.options.multiple = True
# b15.press(
#   page.js.console.log("test"),
#   [page.js.console.log("unlock")])
# b16.press(
#   c.write("Ok"),
#   page.js.console.log("test"),
#   [page.js.console.log("unlock")])
#
# page.ui.layouts.new_line(2)
# # Get button status
# b4 = page.ui.button("test 4")
# b4.click([
#   page.js.console.log(b3.dom.val),
#   page.js.console.log(b16.dom.val),
#   page.js.console.log(b12[0].dom.val),
#   page.js.console.log(b12[1].dom.content),
#   b3.build("Test") # Change value
# ]
# )
#
# # Events
#
# # Change a CSS Style
# b12[0].click([
#   b12[0].dom.css("color", "green")
# ])
#
# # go to another page
#
# # run a service
#
# # add attributes to the url
#
# page.ui.layouts.new_line(1)
# # Other buttons types
page.ui.icons.awesome(icon="fas fa-align-center", text="This is a text")
# page.ui.layouts.new_line(1)
page.ui.buttons.check(label="test")
page.ui.buttons.radio(components.radio.from_list(["A", "B"]))
page.ui.buttons.toggle({'on': "true", 'off': 'false'})
page.ui.buttons.button('Confirm')
page.ui.buttons.important('Important')
#
# c.move()

