
import epyk as pk


# Create a basic report object
page = pk.Page()
page.headers.dev()

modal_confirm = page.ui.modals.validation(page.ui.title("Are you sure you want to delete it ?"))
modal_confirm.add_title("This is a title")

button1 = page.ui.buttons.remove("Show popup 1")
button1.style.css.margin_left = 10
button1.click([
  modal_confirm.dom.show(),
])


modal_confirm = page.ui.modals.acknowledge(page.ui.title("Are you sure you want to delete it ?"))

button2 = page.ui.buttons.remove("Show popup 2")
button2.style.css.margin_left = 10
button2.click([
  modal_confirm.dom.show(),
])

modal_popup = page.ui.modals.popup(page.ui.title("Are you sure you want to delete it ?"))
modal_popup.add(page.ui.texts.paragraph('Test'))

button3 = page.ui.buttons.remove("Show popup 3")
button3.style.css.margin_left = 10
button3.click([
  modal_popup.dom.show(),
])


modal_error = page.ui.modals.error(page.ui.text("Are you sure you want to delete it ?"))

button4 = page.ui.buttons.remove("Show popup error")
button4.style.css.margin_left = 10
button4.click([
  modal_error.dom.show(),
])


modal_info = page.ui.modals.info(page.ui.text("Are you sure you want to delete it ?"))

button5 = page.ui.buttons.remove("Show popup info")
button5.style.css.margin_left = 10
button5.click([
  modal_info.dom.show(),
])

modal_success = page.ui.modals.success(page.ui.text("Are you sure you want to delete it ?"))

button6 = page.ui.buttons.large("Show popup Success")
button6.style.css.margin_left = 10
button6.click([
  modal_success.dom.show(),
])

input = page.ui.input()
input.style.css.text_align = "left"

modal_loading = page.ui.modals.loading("Loading...", options={"background": False})

input.enter([
  modal_loading.build(input.dom.content),
])

button7 = page.ui.buttons.large("Show popup Loading")
button7.style.css.margin_left = 10
button7.click([
  modal_loading.build(input.dom.content),
  modal_loading.dom.show(),
])