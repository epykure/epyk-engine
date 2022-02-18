
import epyk as pk


# Create a basic report object
page = pk.Page()

# Console component
c = page.ui.rich.console(
  "* This is a log section for all the events in the different buttons *", options={"timestamp": True})

page.ui.rich.delta({'number': 100, 'prevNumber': 60, 'thresold1': 100, 'thresold2': 50}, helper="test")
page.ui.texts.up_down({'previous': 240885, 'value': 240985})

number = page.ui.vignets.number(500, "Test")
number.span.add_icon(page.ui.icons.get.ICON_ENVELOPE)
number_2 = page.ui.vignets.number(500, "Test 2 ", options={"url": "http://www.google.fr"})

page.ui.layouts.new_line()
page.ui.div([number, number_2])

page.ui.vignets.block({
  "text": 'This is a brand new python framework', "title": 'New Python Web Framework',
  "button": {"text": 'Get Started', 'url': "/getStarted"}, 'color': 'green'})

v = page.ui.vignets.text({
  "title": "New Python Framework", 'value': "A new Python Web Framework", 'color': 'green',
  'icon': 'fab fa-python', 'colorTitle': 'darkgreen'})

v.click(c.dom.write(v.dom.content))
page.ui.vignets.bubble({"value": 23, "title": "Title"}, helper="This is a helper")
c.move()

