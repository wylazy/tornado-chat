import random
import time
import tornado.web
import tornado.gen
import tornadoredis
from tornado.escape import json_encode
from model.entity import Entity

class LongPollingHandler(tornado.web.RequestHandler):

  def initialize(self):
    self.client = tornadoredis.Client()
    self.client.connect()

  @tornado.web.asynchronous
  def get(self):
    self.get_data()

  @tornado.web.asynchronous
  def post(self):
    self.get_data()
  
  @tornado.gen.engine
  def subscribe(self):
    yield tornado.gen.Task(self.client.subscribe, 'test_channel')
    try :
      self.client.listen(self.on_message)
    except ConnectionError :
      pass;
  
  def get_data(self):
    if self.request.connection.stream.closed():
      return
       
    self.subscribe()

    num = 10
    tornado.ioloop.IOLoop.instance().add_timeout(
      time.time()+num,
      lambda: self.on_timeout(num)
    )


  def on_timeout(self, num):
    self.send_data(json_encode({'name':'', 'msg':''}))
    if (self.client.connection.connected()):
      self.client.disconnect()

  def send_data(self, data):
    if self.request.connection.stream.closed():
      return

    self.set_header('Content-Type', 'application/json; charset=UTF-8')
    self.write(data)
    self.finish()

 
  def on_message(self, msg):
    if (msg.kind == 'message'):
      self.send_data(str(msg.body))
    elif (msg.kind == 'unsubscribe'):
      self.client.disconnect()

  def on_finish(self):
    if (self.client.subscribed):
      self.client.unsubscribe('test_channel');

