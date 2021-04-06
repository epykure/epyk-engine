from epyk.core.Page import Report
from epyk.core.data import components
from epyk.core.css.themes import ThemeBlue
from epyk.core.data import events


# Create a basic report object
page = Report()
page.headers.dev()

template = page.body.add_template(defined_style="doc")
template.style.css.background = page.theme.greys[0]

page.theme = ThemeBlue.BlueGrey()

page.ui.titles.head("Mathematical expressions")

page.ui.paragraph('''
The feature that makes LATEX the right editing tool for scientific documents is the ability to render complex mathematical expressions. 
This page illustrate how to use it to display formulas.
''')

page.ui.texts.formula("\(x^2 + y^2 = z^2\)", align="center")
page.ui.texts.formula(r"$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0$$", align="center")

page.ui.texts.formula(r"$$\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}$$", align="center")
page.ui.texts.formula(r"$$\sqrt[3]{\frac xy}$$", align="center")

page.ui.layouts.hr()
page.ui.titles.subtitle("Report powered by")
page.ui.rich.powered()


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()
