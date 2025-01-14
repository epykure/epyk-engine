
import epyk as pk


# Create a basic report object
page = pk.Page()
page.headers.dev()

page.theme = pk.themes.ThemeBlue.BlueGrey()
d = page.ui.fields.today('test')
i = page.ui.fields.input(placeholder='test2', label='test1')
i2 = page.ui.fields.input('test3', label='test2')
form_modal = page.ui.modals.forms([d, i, i2], "http://127.0.0.1:5000", "POST")
page.ui.buttons.button('SHOW').click(form_modal.show())

privacy_title = page.ui.texts.title('A privacy reminder from Google', 2)
p1 = page.ui.texts.paragraph('''Scroll down and click “%s” when you’re ready to continue to Maps, or explore other options on this page.''' % page.ui.tags.strong('''I agree''', options={'managed': False}))
stroke = page.ui.layouts.hr()
p2 = page.ui.texts.paragraph('''To be consistent with data protection laws, we’re asking you to take a moment to review key points of Google’s Privacy Policy. This isn’t about a change we’ve made — it’s just a chance to review some key points.''')
data_protect = page.ui.texts.title('''Data we process when you use Google''')
l1 = page.ui.texts.paragraph('''When you search for a restaurant on Google Maps or watch a video on YouTube, for example, we process information about that activity - including information like the video you watched, device IDs, IP addresses, cookie data, and location.''')
l2 = page.ui.texts.paragraph('''We also process the kinds of information described above when you use apps or sites that use Google services like ads, Analytics, and the YouTube video player.''')
list_1 = page.ui.lists.list([l1, l2])
process = page.ui.texts.title('''Why we process it''')
p3 = page.ui.texts.paragraph('''We process this data for the purposes described in our %s, including to:''' % page.ui.tags.strong('policy', options={'managed': False}))
l3 = page.ui.texts.paragraph('''Help our services deliver more useful, customized content such as more relevant search results;''')
l4 = page.ui.texts.paragraph('''Improve the quality of our services and develop new ones;''')
l5 = page.ui.texts.paragraph('''Deliver ads based on your interests, including things like searches you've done or videos you've watched on YouTube;''')
l6 = page.ui.texts.paragraph('''Improve security by protecting against fraud and abuse; and''')
l7 = page.ui.texts.paragraph('''Conduct analytics and measurement to understand how our services are used. We also have partners that measure how our services are used. Learn more about these specific advertising and measurement partners.''')
list_2 = page.ui.lists.list([l3, l4, l5, l6, l7])
combining = page.ui.texts.title('''Combining data''')
p4 = page.ui.texts.paragraph('''We also combine data among our services and across your devices for these purposes. For example, we use data from trillions of search queries to build spell-correction models that we use across all of our services, and we combine data to alert you and other users to potential security risks.''')
control = page.ui.texts.title('''Privacy Controls''')
p5 = page.ui.texts.paragraph('''There are many privacy controls you can use, even when you're signed out, to get the Google experience you want.''')
disc = page.ui.modals.disclaimer([privacy_title, p1])
button_show = page.ui.buttons.button('Disclaimer')
button_show.click(disc.show())

