
import epyk as pk


page = pk.Page()

github = page.ui.icon("fab fa-github")
link = page.ui.link("Source code available here", "https://github.com/epykure/epyk-templates")
link.style.css.color = "white"
link.style.css.margin_left = 10
page.ui.banners.top(page.ui.div([github, link]), background=page.theme.notch())

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

b = page.ui.charts.roughviz.bar(languages, y_columns=["rating", 'change'], x_axis='name', width=300)
p = page.ui.charts.roughviz.pie(languages, y_columns=["rating"], x_axis='name', width=300)

