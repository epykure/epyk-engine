
from epyk_studio.core.Page import Report
from epyk.core.css.themes import ThemeBlue


page = Report()
page.headers.dev() # Change the Epyk logo
page.theme = ThemeBlue.BlueGrey()

title = page.ui.title("Epyk a new library to link Python to JavaScript")
paragraph = page.ui.texts.paragraph('''
Thanks to **Epyk Studio** it is easy to start and to write Python code which will then be used to generate rich web pages.
No need to get familiar with all concepts / technologies related to web developmet to start with Epyk. The API will allow to convert your traditional pages to web pages in few minutes.
''', options={"markdown": True})

text = page.ui.text("Epyk will simplify your journey and allow you to learn those concepts !")
text.style.css.color = page.theme.colors[-1]
text.style.css.bold()
text.style.css.font_factor(5)

link = page.ui.link("Epyk Studio", "https://github.com/epykure/epyk-studio")
link.style.css.display = "block"
link.style.css.text_align = "center"
link.style.css.margin_top = 10
link.style.css.margin_bottom = 10

img = page.ui.img(
  "epyklogo_whole_big.png", "https://raw.githubusercontent.com/epykure/epyk-ui/master/epyk/static/images")
img.style.css.height = 50
img.style.css.width = None

container = page.ui.div()
container.extend([title, paragraph, text, link, img])
container.style.css.border = "1px solid %s" % page.theme.colors[3]
container.style.css.padding = 5
container.style.css.margin_top = 10
container.style.standard()