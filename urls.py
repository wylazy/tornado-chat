#coding: utf-8
from handlers.index import MainHandler
from handlers.longpolling import LongPollingHandler

urls = [
  (r'/', MainHandler),
  (r'/longpolling', LongPollingHandler)
]

