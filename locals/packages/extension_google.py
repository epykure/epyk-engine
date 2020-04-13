
from epyk.core.Page import Report
import config

#
from epyk.core.js import Imports
from epyk.core.html import Html

# Extend the current list of packages to include Google charts as a reference
Imports.extend("google-chart", [('loader.js',  'charts/')], version=None, cdnjs_url="https://www.gstatic.com", required=None)

# Create the bespoke HTML component
class Chart(Html.Html):
  # Link this component to the external Javascript module
  __reqJs = ["google-chart"]

  def __init__(self, report, vals, htmlCode=None, width=None, height=None, options=None, profile=None):
    super(Chart, self).__init__(report, vals, htmlCode=htmlCode, css_attrs={"width": width, "height": height})
    self._jsStyles = options or {}

  @property
  def _js__builder__(self):
    # Create the generic build function for those object
    # Those generic Javascrip builder are receiving the below parameters
    #   - htmlObj: The HTML dom object
    #   - data: The value passed in the vals variable
    #   - options: The self._jsStyles object
    # This function is generic and will be used by all the different object created
    # This Js fragment will be used in the refresh and build method
    return '''
      var chart = new google.visualization.AreaChart(htmlObj);
      chart.draw(google.visualization.arrayToDataTable(data), options) '''

  def __str__(self):
    # Load the Google module
    # This module require some specific loading function
    self._report._props.setdefault('js', {}).setdefault("builders", []).append("google.charts.load('current', {'packages':['corechart']})")
    self._report._props.setdefault('js', {}).setdefault("builders", []).append("google.charts.setOnLoadCallback( (function(){return %s}) )" % self.refresh())
    # The HTML component
    return '<div %s></div>' % self.get_attrs(pyClassNames=self.style.get_classes())


# Create a basic report object
rptObj = Report()

# The input data from https://developers.google.com/chart/interactive/docs/gallery/areachart
data = [['Year', 'Sales', 'Expenses'], ['2013', 1000, 400], ['2014', 1170, 460], ['2015', 660, 1120], ['2016', 1030, 540]]

# Create an object on the Javascript side
rptObj.ui.bespoke(Chart, vals=data)

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
