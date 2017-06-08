# http://stackoverflow.com/questions/1301346/what-is-the-meaning-of-a-single-and-a-double-underscore-before-an-object-name




class MyClass():
  def __init__(self):
    self.__superprivate = "Hello"
    self._semiprivate = ", world!"
  
mc = MyClass()
# print mc.__superprivate  >> yields an error!
print mc._semiprivate
print mc.__dict__
