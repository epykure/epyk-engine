import epyk as pk

page = pk.Page()

div = page.ui.div("Text in Div")

div.style.css.bold()  # font_weight: bold
div.style.css.padding_h = 10  # Horizontal padding
div.style.css.underline()  # text_decoration = "underline"
div.style.css.font_factor(10)  # Add X pixel to the default font size

div.style.css.padding_top = 10

page.outs.html_file(name="outHelpers")
