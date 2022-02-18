
import epyk as pk


# Create a basic report object
page = pk.Page()
page.headers.dev()

h = page.ui.titles.head("Skillbars")
u = page.ui.titles.underline()

t1 = page.ui.titles.title("Static Skillbars")
records = [
  {"label": 'python', 'value': 12},
  {"label": 'Java', 'value': 75},
  {"label": 'Javascript', 'value': 80}]
st = page.ui.charts.skillbars(records, y_column='value', x_axis='label')
st.options.percentage = True

t2 = page.ui.titles.title("Dynamic Skillbars")
records = [
  {"label": 'python', 'value': 12},
  {"label": 'Java', 'value': 75},
  {"label": 'Javascript', 'value': 80}]
sk = page.ui.charts.skillbars(records, y_column='value', x_axis='label')

bt = page.ui.button("Update").click([
  sk.build([
    {"label": 'python', 'value': 92},
    {"label": 'Java', 'value': 45},
    {"label": 'Delphi', 'value': 15},
    {"label": 'TypeScript', 'value': 55},
    {"label": 'Javascript', 'value': 82}])
])
