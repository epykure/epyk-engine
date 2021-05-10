# https://www.paypal.com/uk/home

import epyk as pk
import __init__
from ressources import paypal_data


page = pk.Page()
__init__.add_banner(page, __file__)

page.headers.favicon(paypal_data.FAVICON)

page.ui.media.video(paypal_data.VIDEO)

bt = page.ui.banners.text(paypal_data.SLOGAN, background="#0d3685")
bt.style.css.color = "white"

page.ui.vignets.image(paypal_data.VIGNET_1['title'], content=paypal_data.VIGNET_1['content'], image=paypal_data.VIGNET_1['image'], options={"picture": 'right'})

vignet = page.ui.vignets.image(paypal_data.VIGNET_2['title'], content=paypal_data.VIGNET_2['content'], image=paypal_data.VIGNET_2['image'])
vignet.style.css.background_color = '#f5f7fa'

page.ui.vignets.image(paypal_data.VIGNET_3['title'], content=paypal_data.VIGNET_3['content'], image=paypal_data.VIGNET_3['image'], options={"picture": 'right'})


page.ui.banners.text('''
* Subject to status. T&Cs apply. UK residents only.
+ Paying friends back and chipping in requires an account with PayPal. The recipient will need to create an account with PayPal if they don't already have one.
** Buyer Protection is available on eligible purchases only. 180 day time limit and other terms apply.
^ Subject to issuer’s reward programme terms and conditions.
*** Free when sending money to a UK account from a UK account in £GBP. Fees apply when converting currency and when sending money to an account in another country. See fees.
''')

__init__.add_powered(page)