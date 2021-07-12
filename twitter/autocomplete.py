import epyk as pk
from epyk.tests import data_urls

page = pk.Page()
page.body.style.css.padding_h = 10  # Add padding to the body
# get data from external github repository and create a filter group
records = page.py.requests.csv(data_urls.DEMO_COUNTRY)
grp = page.data.js.record(records).filterGroup("aggData")
# Autocomplete component.
countries = page.ui.inputs.autocomplete(placeholder="select a country")
countries.options.source = sorted(list(set([rec['Country Name'] for rec in records])))
# container to store the selected items when enter is pressed.
cols_keys = page.ui.lists.drop(html_code="cols_agg_keys")
cols_keys.style.css.min_height = 20
cols_keys.items_style(style="bullets")
cols_keys.drop()
# enter event on the input autocomplete component.
countries.enter([cols_keys.dom.add(countries.dom.content), countries.dom.empty()])
# write result to static file.
page.outs.html_file(name="outAutocomplete")
