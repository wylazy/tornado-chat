#coding:utf-8

from urls import urls
import tornado.web 
import os

SETTINGS = dict(
  template_path = os.path.join(os.path.dirname(__file__), "templates"),
  static_path = os.path.join(os.path.dirname(__file__), "static"),
  cookie_secret = "Y2FjM2Y5MzgwNTBiMDEwMzAxNGU5MWI4NDE2OTk0ODkK",
  debug = True
)

application = tornado.web.Application(handlers = urls,
    **SETTINGS
)

