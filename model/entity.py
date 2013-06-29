
class Entity(object) :
  def __init__(self, name) :
    self.name = name

  @staticmethod
  def get(name) :
    return Entity(name)
