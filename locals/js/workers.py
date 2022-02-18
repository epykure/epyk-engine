
import epyk as pk
from epyk.mocks import randoms


# Create a basic report object
page = pk.Page()

page.ui.components_skin = {
  "titles.underline": {"css": {"border-bottom-color": "#f0db4f", "margin-bottom": "10px"}},
  "button": {"css": {"background": "#323330", "color": "#f0db4f", "border-color": "#323330"}}}

page.ui.title("JavaScript Workers")
page.ui.titles.underline()
h = page.ui.texts.highlights('''
Example of Python script using web workers.
  ''', icon="fab fa-js", type="info", options={"close": False})
h.style.css.background = "#f0db4f"

w = page.js.worker()
w.connect(content='''
self.addEventListener('message', function(e) {
  var data = e.data;
  switch (data.cmd) {
    case 'start':
      self.postMessage('WORKER STARTED TEST: ' + data.msg);
      break;
    case 'stop':
      self.postMessage('WORKER STOPPED: ' + data.msg + '. (buttons will no longer work)');
      self.close(); /* Terminates the worker. */
      break;
    default:
      self.postMessage('Unknown command: ' + data.msg);
  };
}, false);
''')

div = page.ui.div()
page.ui.button("Say HI").click([w.postMessage({'cmd': 'start', 'msg': 'Hi'})])
page.ui.button("Send unknown command").click([w.postMessage({'cmd': 'test', 'msg': 'test'})])
page.ui.button("Stop worker").click([w.postMessage({'cmd': 'stop', 'msg': 'Bye'})])

t1 = page.ui.title("Display dynamic text")
t1.style.css.margin_top = 10

input = page.ui.inputs.left(placeholder="put you name and click Hi")
page.ui.button("Hi").click([
  w.postMessage(pk.js_datamap([(input, 'msg')], {'cmd': 'start'}))])
w.on('message', [div.build(w.message)])

series = randoms.getSeries(4, 100)


page.ui.title("Histogram")
hist = page.ui.charts.plotly.histogram(series, y_columns=[1, 2, 3])

w2 = page.js.worker()
w2.connect(content='''
self.addEventListener('message', function(e) {
  var data = e.data; console.log(data);
  switch (data.cmd) {
    case 'add':
      self.postMessage('Result: ' + (data.value1 + data.value2 + data.value3)); break;
    case 'mult':
      self.postMessage('Result: ' + (data.value1 * data.value2 * data.value3)); break;
    case 'stop':
      self.postMessage('WORKER STOPPED: ' + data.msg + '. (buttons will no longer work)');
      self.close(); break;
    default:
      self.postMessage('Unknown command: ' + data.msg);
  };
}, false);
''')


slider = page.ui.slider()
slider.options.slide()

number = page.ui.fields.number()

div = page.ui.div()
page.ui.button("Add").click([
  w2.postMessage({'cmd': 'add', 'value1': 2}, components=[(slider, "value2"), (number, "value3")])])
page.ui.button("Mult").click([
  w2.postMessage({'cmd': 'mult', 'value1': 5}, components=[(slider, "value2"), (number, "value3")])])

page.ui.button("Stop worker").click([w2.postMessage({'cmd': 'stop'})])

w2.on('message', [div.build(w2.message)])


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()
