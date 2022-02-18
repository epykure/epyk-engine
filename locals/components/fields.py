
from epyk.core.Page import Report
from epyk.core.data import components


# Create a basic report object
page = Report()
page.headers.dev()

a = page.ui.fields.select(components.select.from_list(["Apple", 'Orange']), label="test", helper="select fruit",
                          options={"align": 'center'})#
a.input.attr["data-live-search"] = "true"

page.ui.fields.date('2020-04-08', label="Date").included_dates(["2020-04-08", "2019-09-06"])

page.ui.fields.today(label="Date").included_dates(["2019-09-01", "2019-09-06"])

page.ui.fields.now(label="timestamp", color="red", helper="This is the report timestamp")

page.ui.fields.time(label="timestamp", color="red", helper="This is the report timestamp")

page.ui.fields.input("", label="Range Example", icon="fas fa-unlock-alt")

page.ui.fields.input("", label="Range Example", icon="fas fa-unlock-alt")

page.ui.fields.static(label="readonly field")

page.ui.fields.integer(label="test")

page.ui.fields.password(label="password")

page.ui.fields.textarea(label="Date")

page.ui.fields.checkbox(True, label="Check")

page.ui.fields.radio(False, label="Radio")

page.ui.fields.range(54, min=20, label="Range Example", icon="fas fa-unlock-alt")

