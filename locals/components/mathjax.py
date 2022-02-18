
import epyk as pk


# Create a basic report object
page = pk.Page()
page.headers.dev()


h = page.ui.titles.head("Maths")
u = page.ui.titles.underline()
f = page.ui.texts.formula("$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}.$$", helper="This is a formula")

input = page.ui.input("$$x = {-b \pm \sqrt{b^2-5ac} \over 2a}.$$")
bt = page.ui.button("Update")
bt.click([
  f.build(input.dom.content)
])


bc = page.ui.button("Clear")
bc.click([
  f.js.typesetClear()
])

t2 = page.ui.titles.title("Pythagorean theorem")
f2 = page.ui.texts.formula("$$ x^2 + y^2 = z^2 $$", helper="This is a formula")


t3 = page.ui.titles.title("Mass-energy equivalence")
f3 = page.ui.texts.formula("$$ E=mc^2 $$", align="center", helper="This is a formula")

