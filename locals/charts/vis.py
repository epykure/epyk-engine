
import epyk as pk
import random
import __init__


# Test module to get test data
from epyk.tests import data_urls


# Create a basic report object
page = pk.Page()
page.headers.dev()
__init__.add_banner(page, __file__)


def getSeries(count, size, negatives=0.1, missing=0.2):
  data = []
  #
  neg = size * [False]
  miss = size * [False]
  for s in range(size):
    data.append({"x": s})
    for c in range(count):
      if miss[s]:
        continue

      data[-1][c] = random.randint(0, 10000) / 100 * (-1 if neg[s] else 1)
  return data


data_world = page.py.requests.json(data_urls.WORLD_INDEX)

data = getSeries(5, 10)

# network = page.ui.charts.vis.network(data, y_columns=list(range(4)), x_axis='x')


line = page.ui.charts.vis.line(data, y_columns=list(range(4)), x_axis='x')
bar = page.ui.charts.vis.bar(data, y_columns=list(range(4)), x_axis='x')
scatter = page.ui.charts.vis.scatter(data, y_columns=list(range(4)), x_axis='x')


surface = page.ui.charts.vis.surface(data, y_columns=[1, 2], x_axis='x', z_axis=0)
line3d = page.ui.charts.vis.line3d(data, y_columns=[1, 2], x_axis='x', z_axis=0)
bar3d = page.ui.charts.vis.bar3d(data, y_columns=[1, 2], x_axis='x', z_axis=0)
scatter3d = page.ui.charts.vis.scatter3d(data, y_columns=[1, 2], x_axis='x', z_axis=0)

network = page.ui.charts.vis.network()
network.add_node("A")
network.add_node("B")
network.add_edge(0, 1)

network.onReady([
  network.js.setData({"nodes": [{"id": 0, "label": "test"}], "edges": []}),
])

bt = page.ui.button("click").click([
  network.js.setData({"nodes": [{"label": "hahaha"}], "edges": []}),
])

box = page.ui.div()
box.style.css.background = "white"
box.style.css.padding_left = 10
box.style.css.padding_right = 10
box.extend([[line, bar, scatter]])
box.extend([bar3d, scatter3d])
box.add(surface)
box.add(line3d)
box.extend([bt, network])
box.style.configs.doc()
__init__.add_powered(page)

