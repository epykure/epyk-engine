
import epyk as pk


# Create a basic report object
page = pk.Page()

div = page.ui.div("toto")

div.style.css_class.media({div: {"background-color": "red"}}, 'only', 'screen', {"and": [{'max-width': '600px'}]})
div.style.css_class.media({div: {"background-color": "blue"}}, 'only', 'screen', {"and": [{'min-width': '800px'}]})

button = page.ui.buttons.button('Contact Sales')
imp = page.ui.buttons.important('Get Started for Free')
nav = page.ui.navigation.bar(title="test")
nav.add_text("This is a huge text that I don't know what to do with")
nav + button
nav + imp

nav.style.css_class.media(
  {nav: {"float": "none", 'width': '100%'}}, 'only', 'screen', {"and": [{'max-width': '600px'}]})
