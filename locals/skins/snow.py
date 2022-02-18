from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

page.body.style.css.background = "Blue"

page.skins.winter()

page.ui.button("Load")