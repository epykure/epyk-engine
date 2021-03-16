
from epyk.core.Page import Report
from epyk.core.css.themes import ThemeBlue


# Create a basic report object
page = Report()
page.headers.dev()
page.theme = ThemeBlue.BlueGrey()
page.body.add_template(defined_style="doc")

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
      self.close(); // Terminates the worker.
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
w.on('message', [div.build(w.message)])

page.ui.layouts.hr()
page.ui.titles.subtitle("Report powered by")
page.ui.rich.powered()


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()
