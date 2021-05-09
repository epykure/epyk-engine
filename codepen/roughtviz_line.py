import epyk as pk

page = pk.Page()
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
b = page.ui.charts.roughviz.plot(languages, y=["rating", 'change'], x='name', width=300)
page.outs.codepen()