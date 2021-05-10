
from epyk_studio.core.Page import Report
from epyk.core.css.themes import ThemeDark


page = Report()
page.inputs = {"lang": 'fr', 'theme': 'ThemeBlue.Blue'}

s = page.studio.themes()
l = page.studio.langs()


nav = page.studio.nav(title="Code Betas")
nav.add_right(l)
nav.add_right(s)

page.studio.vitrine.cover(r"C:\Users\olivier\Documents\GitHub\epyk-templates\static\assets\header.PNG")


b = page.studio.button("Test")

page.body.onReady([
  b.dom.events.trigger("click", options={"timer": 10})
])

t1 = page.ui.text("TTTTTTTTTTT")
t2 = page.ui.text("2222222222222")

# page.ui.icons.timer(2, [
#   page.js.console.log("Test")
# ])

page.ui.buttons.live(2, [
  page.js.console.log("live")
])

t1.style.effects.fade_out()
t2.style.effects.fade_in()

page.ui.div([
  t1, t2
])

b = page.ui.button("Click").click([
  #t1.dom.css("animation", "fade_in 2s ease-in-out 1 normal forwards"),
  #t2.dom.css("animation", "fade_out 2s ease-in-out 1 normal forwards"),

  t1.dom.css("display", "none"),
  t2.dom.css("animation-name", "fade_out"),
  t2.dom.effects.blink(),
  #t2.dom.css("display", "none"),
  t1.dom.css("animation-name", "fade_in"),
])
b.style.css.opacity = 0

txt1 = page.studio.text('''
The goal of Epyk is to ensure the implementation of a coherent system using a minimum of layers. With Epyk the user stays in the Python layer to drive and optimize the data transformation. This Framework also encourages the implementation of Micro services and cloud based architecture.
''')
txt2 = page.studio.text("ok 2")

car = page.studio.carousel([txt1, txt2], options={"timer": 2})

#page.studio.gallery.carousel([txt1, txt2]+["https://colorlib.com/preview/theme/photographer/img/portfolio/%s.jpg" % i for i in range(1, 20)])

page.studio.gallery.mosaic(
  ["https://colorlib.com/preview/theme/photographer/img/portfolio/%s.jpg" % i for i in range(1, 20)]
, options={"zoom": True})

print(car.clear_timer.toStr())
b.click([
  page.js.console.log("Test"),
  car.clear_timer
])

body = page.studio.container()
body + page.studio.vitrine.vignet("Python expertise", content="", image=r"C:\Users\olivier\Documents\GitHub\epyk-templates\static\assets\header.PNG")
py = page.studio.vitrine.card("Python expertise", content="", icon="fab fa-python", render="col")
py.style.css.opacity = 0

js = page.studio.vitrine.card("Javascript expertise", content="", icon="fab fa-js-square", render="col")
body + page.ui.title("Two main languages")
body + page.studio.row([py, js])
body + page.ui.title("Personal support based on challenges")

page.studio.banner([
  page.ui.title("Be part of the Code Betas community")
])

t4 = page.ui.title("Testtttttttttttttttttttt")
t4.style.css.opacity = 0

page.body.scroll([
  #page.js.console.log(page.js.window.scrollY),
  t4.dom.onViewPort([t4.dom.effects.fade_in()]),
  py.dom.onViewPort([py.dom.effects.fade_in()]),
  b.dom.onViewPort([b.dom.effects.fade_in()]),
])

body2 = page.studio.container()
body2 + t4

page.studio.vitrine.disclaimer()