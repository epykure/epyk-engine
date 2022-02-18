
from epyk.core.Page import Report

from epyk.mocks import urls as data_urls


page = Report()
page.headers.dev()

menu = page.ui.layouts.icons()
menu.add_icon("fab fa-accusoft")
menu.add_icon("fab fa-accusoft")

menu.icon.click([menu.icon.dom.css({"color": 'red'})])

page.ui.icons.signin("RRR")

env = page.ui.icons.awesome(page.ui.icons.get.ICON_ENVELOPE, text=2)
#env.icon_css({"background": 'MistyRose', 'font-size': '20px'})
#env.span.style.addCls("fa-layers-counter")

edit = page.ui.icons.edit()
edit.click([page.js.console.log('test')])

page.ui.icons.clock().css({"color": 'blue'})
#page.ui.icons.edit().color("red")

