
from epyk.core.Page import Report
from epyk.core.css.themes import ThemeBlue


# Create a basic report object
page = Report()
page.headers.dev()
page.theme = ThemeBlue.BlueGrey()
page.body.add_template(defined_style="doc")

page.ui.components_skin = {"button": {"css": {"background": "#323330", "color": "#f0db4f", "border-color": "#323330"}}}

page.ui.title("JavaScript - Transitions and transforms")

i = page.ui.fields.input("", label="Range Example", icon="fas fa-unlock-alt")

page.ui.button("Translate").click([
  i.label.dom.transition('margin-left', '100px', 2, reverse=True),
  i.label.dom.transition('color', 'red', 5, reverse=True)
])


page.ui.button("Opacity").click([
  i.label.dom.css({'WebkitTransition': 'opacity 1s'}),
])


page.ui.button("Skew").click([
  i.label.dom.transform.skewX(20),
])


page.ui.button("Rotate").click([
  i.label.dom.transform.rotate(90),
])

page.ui.layouts.hr()
page.ui.titles.subtitle("Report powered by")
page.ui.rich.powered()


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()
