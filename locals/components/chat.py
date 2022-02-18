# error
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()


container = page.ui.network.chat(html_code='chat_service')
