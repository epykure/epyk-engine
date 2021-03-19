"""
Common module for all the static data used in the different tests
"""

import os
import random
import json
import webbrowser

# Deduce the \outs folder based on this module path
# the \outs folder is excluded from Git
TESTS_PATH = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATHS = r"%s\outs" % TESTS_PATH
OUTPUT_PATHS_LOCALS_SLIDES = r"%s\outs\slides" % TESTS_PATH
OUTPUT_PATHS_LOCALS_HTML = r"%s\outs\html" % TESTS_PATH
OUTPUT_PATHS_LOCALS_TS = r"%s\outs\ts" % TESTS_PATH
OUTPUT_PATHS_LOCALS_INTERACTIVE = r"%s\interactives\front_end" % TESTS_PATH
OUTPUT_TEMPS = r"C:\tmps"
OUT_FILENAME = 'report_example'

SERVER_DATA_HOST = '192.168.0.34'
SERVER_DATA_PORT = 8085

SERVER_SOCKET_HOST = "127.0.0.1"
#SERVER_SOCKET_HOST = '192.168.0.34'
SERVER_SOCKET_PORT = 5000

# The path to the target applications
ANGULAR_APP_PATH = None # r"C:\Angular\testApp"
VUE_APP_PATH = None # r"C:\Vue\vue-apps-new"

#
FAVICON_URL = r"https://raw.githubusercontent.com/epykure/epyk-templates/master/static/images/logo.ico"
IMG_PATH = "https://raw.githubusercontent.com/epykure/epyk-ui/master/epyk/static/images"

# Extra static information with the links of the different external websites
URL_w3c = r"https://www.w3schools.com/html/tryit.asp?filename=tryhtml_basic"
URL_CODEPEN = r"https://codepen.io/"
URL_JSFIDDLE = r"https://jsfiddle.net/"

# Example files definition
MAP_COLS = {'flights.txt': {"distance": float, 'delay': float}}


def open_url(url):
  """
  Small utilities to open the browser to a specific web page.
  Some url are predefined and they are there to facilitate the testing of the generated Html pages

  :param url: A url

  """
  webbrowser.open(url)


def get_data(name, n=None, map_cols_type=None):
  """
  Load the static files used to test the different function.
  Files can be json or txt file (with header and delimited with a ,)

  :param name: THe filename
  :param n: Integer the max number of records
  :param map_cols_type: Dictionary. Special column type mapping

  :return: A record (A list of dictionaries)
  """
  if name.endswith(".json"):
    return json.load(open(os.path.join(TESTS_PATH, "data", name)))

  map_cols_type = map_cols_type or MAP_COLS.get(name, {})
  records = []
  with open(os.path.join(TESTS_PATH, "data", name)) as file:
    header = file.readline().strip().split(",")
    for i, line in enumerate(file):
      if n is not None and i > n:
        return records

      rec = dict(zip(header, line.strip().split(",")))
      for c, t in map_cols_type.items():
        rec[c] = t(rec[c])
      records.append(rec)
  return records


def getSeries(count, size, negatives=0.1, missing=0.2):
  data = []
  #
  neg = size * [False]
  miss = size * [False]
  for s in range(size):
    data.append({"x": s, 'r': random.randint(0, 10), 'g': random.randint(0, 5)})
    for c in range(count):
      if miss[s]:
        continue

      data[-1][c] = random.randint(0, 10000) / 100 * (-1 if neg[s] else 1)
  return data
