
import epyk as pk


# Create a basic report object
page = pk.Page()
page.headers.dev()


# page.ui.forms.inputs([
#   {"label": "name", "htmlCode": "input"},
#   {"label": "name 2", "htmlCode": "input2"},
# ]) # , "http://127.0.0.1:5000", "POST"

t = page.ui.text("youpi").editable()
#r = page.ui.select([
#  {"name": 'Test', 'value': "false"},
#  {"name": 'Test 2', 'value': "true"},
#])

#page.ui.button("Test").click([
#  page.js.console.log(r.dom.val),
#  t.dom.contentEditable(r.dom.content)
#])

#print(page.ui.text("youpi").dom.contentEditable(True))
#page.ui.forms.date("http://127.0.0.1:5000", "POST")
#page.ui.forms.dates("http://127.0.0.1:5000", "POST")
b = page.ui.button("Run").css({"width": "100px"})

#s = page.ui.select(["A", "B"])
n = page.ui.layouts.new_line()
#s.set_attrs({"name": "ok"})
#f = page.ui.layouts.form([n])
#f += f.submit

b.click([
  page.js.console.log(page.js.objects.mouseEvent.offsetX),
  page.js.console.log(page.js.objects.mouseEvent.getField("type"))
])

#popup = page.ui.layouts.popup(page.ui.title('Test'), color="red")
#popup + page.ui.texts.paragraph('Test')

# page.ui.forms.input("")

# popup = page.ui.layouts.popup(page.ui.title('Test'), color="red")
# popup + page.ui.texts.paragraph('Test')


# page.py.requests.http_server(5000)