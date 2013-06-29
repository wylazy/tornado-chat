#!/usr/bin/python
# -*- coding: utf-8 -*-
"""web server"""

import tornado.ioloop
import sys
from application import application

PORT = '3021'
if __name__ == "__main__":
  application.listen(PORT) 
  print 'Server is running http://localhost:%s/' % PORT
  tornado.ioloop.IOLoop.instance().start()

