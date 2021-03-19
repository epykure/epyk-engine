from epyk.core.Page import Report
from epyk.core.data import components
from epyk.core.css.themes import ThemeBlue
from epyk.core.data import events


# Create a basic report object
page = Report()
page.headers.dev()
page.body.add_template(defined_style="doc")
page.theme = ThemeBlue.BlueGrey()

categories = ["Shopping", "Meeting"]

page.ui.title("My todo list")
check_list = page.ui.lists.checks(width=(100, "%"))
check_list.options.delete = True
check_list.style.css.border = True
check_list.style.css.padding = 5

item = page.ui.inputs.left(placeholder="Add your item", width=(None, ''))
category = page.ui.select(components.select.from_list(categories))
button = page.ui.buttons.colored("Add")
page.css.customText('''.test:hover {color: green !IMPORTANT; font-size:20px  !IMPORTANT}''')

container = page.ui.div()
for c in [item, category, button]:
  container.add(page.ui.layouts.inline(c))
container[1].style.css.padding_left = 5
container[1].style.css.padding_right = 5

page.ui.lists.menu(check_list)
item.enter([button.dom.events.trigger("click")])

clear = page.ui.buttons.colored("Clear").css({"margin-right": '5px'}).click([check_list.dom.clear()])
save = page.ui.buttons.colored("Save")
page.ui.div([clear, save], align="center")

c = page.ui.rich.console(
  "* This is a log section for all the events in the different buttons *", options={"timestamp": True})
save.click([c.dom.write(check_list.dom.content)])
button.click([
  check_list.dom.add(item),
  # add dynamic content
  check_list.dom.contextMenu(["Test 1", "Test 2"],
                             menuJsFncs=[
                               c.dom.write(events.data.stringify()),
                               c.dom.write(events.data.stringify()),
                             ]),
  check_list.dom.tags(category.dom.content, css_cls="test")
])

page.ui.layouts.hr()
page.ui.titles.subtitle("Report powered by")
page.ui.rich.powered()


if __name__ == "__main__":
    # If the script is run directly for Python.
    page.outs.html_file()
