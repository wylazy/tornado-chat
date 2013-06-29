
from tornado.escape import json_encode
from entity import Entity

v = Entity.get('aaa')
print json_encode(v.__dict__)
