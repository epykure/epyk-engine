
import epyk as pk
from epyk.core.data.Data import DataJs
from epyk.core.data import components


# Create a basic report object
page = pk.Page()
page.headers.dev()
page.theme = pk.themes.ThemeBlue.BlueGrey()

page.ui.title("JavaScript - Data Filtering")

h = page.ui.texts.highlights(
  "This illustrates how to filter data for containers like tables and charts from JavaScript",
  icon="fab fa-js", type="info", options={"close": False})
h.style.css.background = "#f0db4f"

languages = [
  {"name": 'C', 'type': 'code', 'rating': 17.07, 'change': 12.82},
  {"name": 'Java', 'type': 'code', 'rating': 16.28, 'change': 0.28},
  {"name": 'Python', 'type': 'script', 'rating': 9.12, 'change': 1.29},
  {"name": 'C++', 'type': 'code', 'rating': 6.13, 'change': -1.97},
  {"name": 'C#', 'type': 'code', 'rating': 4.29, 'change': 0.3},
  {"name": 'Visual Basic', 'type': 'script', 'rating': 4.18, 'change': -1.01},
  {"name": 'JavaScript', 'type': 'script', 'rating': 2.68, 'change': -0.01},
  {"name": 'PHP', 'type': 'script', 'rating': 2.49, 'change': 0},
  {"name": 'SQL', 'type': 'script', 'rating': 2.09, 'change': -0.47},
  {"name": 'R', 'type': 'script', 'rating': 1.85, 'change': 0.90},
]

filter_column = "type"

select = page.ui.select(components.select.from_records(languages, column=filter_column))
table = page.ui.tables.tabulator(languages)

filter_data = DataJs(page).record(data=languages)

select.change([
  table.build(filter_data.filterGroup("test").equal(filter_column, select.dom.content))
])


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()
