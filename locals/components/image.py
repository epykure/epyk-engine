
from epyk.core.Page import Report
from epyk.core.css.themes import ThemeDark

import config

# Create a basic report object
page = Report()
page.headers.dev()

# Change the theme of the report
page.theme = ThemeDark.Dark()

# Change the first color of this theme (overrride)
page.theme.colors[-1] = "yellow"

# Add icon
# The path for the icon is defind in config
page.ui.images.circular("epykIcon.PNG", path=config.IMG_PATH)

page.ui.layouts.new_line()

# Avatar with a status
page.ui.images.avatar("Epyk", status='out')


# Avatar with an image
page.ui.images.avatar(image="epykIcon.PNG", path=config.IMG_PATH, status=False)

# Add badges
page.ui.layouts.new_line()
page.ui.images.badge("Test badge", "Label", icon="fas fa-align-center")

page.ui.layouts.new_line()
page.ui.images.badge("This is a badge", background_color="red", color="white")

page.ui.layouts.new_line()
page.ui.images.badge(12, icon="far fa-bell", options={"badge_position": 'left'})

# Add a carousel of images
car = page.ui.images.carousel(["epykIcon.PNG", "epyklogo.ico", "epyklogo_whole_big.png"], path=config.IMG_PATH, height=(200, 'px'))
car.click([page.js.console.log('data', skip_data_convert=True)])

# Add a simple badge
c1 = page.ui.images.badge(3, icon="far fa-bell", url="test")
c1.style.display = None

# Add the badge to a container on the right
page.ui.layouts.div([c1], align='right')
page.ui.button("display").click(c1.dom.toggle())

# Add an emoji
page.ui.images.emoji(page.symbols.smileys.DISAPPOINTED_FACE)

# Add an animated picture
a = page.ui.images.animated("epykIcon.PNG", text="This is a comment", title="Title", url="#", path=config.IMG_PATH)
a.style.css.borders()

img = page.ui.img("epykIcon.PNG", path=config.IMG_PATH, align="right", width=(200, "px"))
img.style.css.border = "1px solid black"

page.ui.layouts.br(2)

# Add multiple badge on the same row
page.ui.images.badge("306", url="google", icon="fas fa-align-center", options={'badge_css': {'color': 'white', "background": 'red'}})
page.ui.images.badge("306", url="google", icon="fas fa-align-center", options={'badge_css': {'color': 'white', "background": 'orange'}})
page.ui.images.badge("306", url="google", icon="fas fa-align-center", options={'badge_css': {'color': 'white', "background": 'red'}})
page.ui.images.badge("306", url="google", icon="fas fa-align-center", options={'badge_css': {'color': 'white', "background": 'red'}})
b = page.ui.images.badge(7688, icon="fab fa-python", options={'badge_css': {'color': 'white', "background": 'red'}})
b.options.badge_css = {"background": 'green'}

i = page.ui.layouts.icons(["fas fa-align-center", 'fab fa-python'])
i.icon.click([i.icon.dom.css({"color": 'red'})])

t = page.ui.text("Test")
t.style.font_size = 20
t.style.effects.translate(1)

# Add the epyk icon
page.ui.icons.epyk()

