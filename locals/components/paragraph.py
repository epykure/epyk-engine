
from epyk.core.Page import Report

page = Report()
page.headers.dev()

page.body.style.globals.size = 14

#
from epyk.core.css import Defaults

#Defaults.Font.size = 14

#

# Console component
c = page.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

page.ui.contents()

page.ui.title("Python (programming language)", level=1)

a = page.ui.tags.a('Python', "", options={'managed': False})
a.preview("https://en.wikipedia.org/api/rest_v1/page/summary/Python")


page.ui.texts.paragraph('''
**%s** is an [interpreted](https://en.wikipedia.org/wiki/Interpreted_language), high-level, general-purpose [programming language](https://en.wikipedia.org/wiki/Programming_language). 
Created by [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum) and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. 
Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.<sup>[28]</sup>

Python is dynamically typed and garbage-collected. 
It supports multiple programming paradigms, including structured (particularly, procedural,) object-oriented, and functional programming. 
Python is often described as a "batteries included" language due to its comprehensive standard library.%s
''' % (a.html(), page.ui.tags.sup("[29]", options={'managed': False})), helper="Paragraph helper", options={'markdown': True})


page.ui.title("History", level=2)

p = page.ui.texts.paragraph('''
Python was conceived in the late 1980s[34] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC language (itself inspired by SETL),[35] capable of exception handling and interfacing with the Amoeba operating system.[8] 
Its implementation began in December 1989.[36] Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his "permanent vacation" from his responsibilities as Python's Benevolent Dictator For Life, a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker.[37] 
He now shares his leadership as a member of a five-person steering council.[38][39][40] 
In January 2019, active Python core developers elected Brett Cannon, Nick Coghlan, Barry Warsaw, Carol Willing and Van Rossum to a five-member "Steering Council" to lead the project.[41]
''')


page.ui.texts.paragraph('''
The language's core philosophy is summarized in the document The Zen of Python (PEP 20), which includes aphorisms such as:[55]
''')

page.ui.lists.disc([
  'Beautiful is better than ugly.',
  'Explicit is better than implicit.',
  'Simple is better than complex.',
  'Complex is better than complicated.',
  'Readability counts.'
])


# div.on('mouseenter', [
#   page.js.request_http("test", 'GET', "https://en.wikipedia.org/api/rest_v1/page/summary/Python").send(),
#   page.js.console.log("test", skip_data_convert=True),
#   page.js.createElement("div", "popup").innerHTML('''
#     An interpreted language is a type of programming language for which most of its implementations execute instructions directly and freely, without previously compiling a program into machine-language instructions. The interpreter executes the program directly, translating e
#     ''').attr('id', 'popup').css({
#         'color': 'red', 'display': 'block', 'background': 'white', 'width': '250px', 'padding': '10px'}).position(),
#   page.body.dom.appendChild(page.js.object("popup")),
# ])
#
# div.on('mouseleave', [
#   page.js.getElementById("popup").remove()
# ])

page.ui.button("Test").click([
  c.dom.write(p.dom.content),
  p.refresh()
])

c.move()

