import os


def add_banner(page, fp, position="bottom"):
  path, filename = os.path.split(fp)
  github_path = r"https://github.com/epykure/epyk-templates/tree/master/websites"
  github = page.ui.icon("fab fa-github")
  link = page.ui.link("Source code available here", "%s/%s" % (github_path, filename))
  link.style.css.color = "white"
  link.style.css.margin_left = 10
  if position == "bottom":
    page.body.style.css.padding_bottom = 70
    page.ui.banners.bottom(page.ui.div([github, link]), background=page.theme.notch())
  else:
    page.body.style.css.margin_top = 40
    page.ui.banners.top(page.ui.div([github, link]), background=page.theme.notch())

  qrcode = page.ui.qrcode(github_path)
  qrcode.style.css.fixed(bottom=60, left=60)
  qrcode.style.css.cursor = "pointer"
  qrcode.style.css.z_index = 300


def add_powered(page):
  tag = page.ui.rich.powered()
  tag.style.css.margin_bottom = 5
  tag.style.css.margin_top = 5
