
from epyk.core.Page import Report

page = Report()

anchor = page.ui.title("This is a video")
vignet = page.ui.vignets.video(
  'toto', 'Video', r"/static/SGHV5530.MP4", height=200)

vignet.video.options.controls = True
vignet.video.sticky(anchor)
page.ui.layouts.br(100)


