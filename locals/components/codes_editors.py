
import epyk as pk


# Create a basic report object
page = pk.Page()
page.headers.dev()

t1 = page.ui.title("CSS Code Editor")
c1 = page.ui.codes.css('''
.cssdivnoborder {margin: 0 ;clear: both ;padding: 0 ;border: 0 ;}
.cssdivnoborder:focus {outline: 1px solid #B4BABF ;}
''')


t2 = page.ui.title("XML Code Editor")
c2 = page.ui.codes.xml('''
<?xml version="1.0" encoding="UTF-8"?>
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>
''', height=100)


t3 = page.ui.title("Python Code Editor (Readonly)")
py_code = page.ui.codes.python('''
from epyk.core.Page import Report

page = Report()
page.headers.dev()
''', height=50)
py_code.options.readOnly = True

