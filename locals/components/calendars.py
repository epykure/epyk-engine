
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

page.ui.titles.headline("Daily")

content = {
  "2020-07-02": {'task1': 50, 'task2': 50},
  "2020-07-03": {'task1': 100},
  "2020-07-21": {'task4': 100},
  "2020-07-22": {'task4': 100}
}

july = page.ui.calendars.days(7, content, align="center", options={"colors": {"task4": 'red'}})

july.task('task1', start="2020-07-10", capacity=[50, 30, 10, 80])
july.task('task3', start="2020-07-20", capacity=[50, 40, 10])

july.weekly("task6", start="2020-07-02", capacity=3, frequency=2, options={'unit': 8})

page.ui.calendars.legend(july.tasks)

july.style.css.margin = "0 5px"

august = page.ui.calendars.forecast(4, content, options={"colors": {"task4": 'red'}})
august.style.css.margin = "0 5px"

page.ui.row([july, august], position="top")

page.ui.titles.headline("Montly")

records = {
  1: {"Project 1": 12, "Project 2": 30},
  2: {"Project 1": 12, "Project 2": 30},
  3: {"Project 1": 42, "Project 2": 30},
  4: {"Project 1": 15, "Project 2": 30},
  5: {"Project 1": 12, "Project 2": 30},
  6: {"Project 1": 12, "Project 2": 30},
  7: {"Project 1": 12, "Project 2": 30},
}

monthly = page.ui.calendars.months(content=records, align="center")
page.ui.calendars.legend(monthly.tasks)

monthly.style.css.margin_top = 10

update = page.ui.rich.update()
page.ui.button("Click").click([update.refresh()])

pill = page.ui.calendars.pill("4D")
page.ui.button("Click").click([page.js.alert(pill.dom.content)])
