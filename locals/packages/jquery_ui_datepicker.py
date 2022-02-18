
import epyk as pk


page = pk.Page()
page.headers.dev()

# Console component
c = page.ui.rich.console(
  "* This is a log section for all the events in the different buttons *", options={"timestamp": True})

# Add a date picker object based on the current date
date1 = page.ui.fields.today(label="Date 1")
date1.included_dates(["2020-04-04"])

# Add a date picker object based on the current date
date2 = page.ui.fields.today(label="Date 2")
date2.excluded_dates(["2020-04-04"])

# Add a date picker object based on theclose of business date
date3 = page.ui.fields.cob(label="Date 3")

# Add a fixed date picker object
date4 = page.ui.fields.date("2020-01-01", label="Date 4")
# Add some options from the documentation https://api.jqueryui.com/datepicker/#option-showWeek
date4.input.options.showWeek = True
date4.input.options.showOtherMonths  = True

# Button and transofmation on the datepicker components
page.ui.button("click").click([
  c.dom.write(date1.input.dom.val, stringify=True),
  c.dom.write(date2.input.dom.content),

  # Some Javascript conversion functions
  c.dom.write(date2.input.dom.content.date.getTime()),
  c.dom.write(date2.input.dom.content.date.getMonthName()),
])

# Button and transformation on the datepicker components
page.ui.button("Disable").click([
  date2.input.js.show(),
  date2.input.js.enable(),
  date2.input.js.refresh(),
])

# Button and transofmation on the datepicker components
page.ui.button("Set Date").click([
  date3.input.build("1985-09-24"),
  date2.input.js.disable(),
  c.dom.write("date 2 disabled")
])

c.move()

