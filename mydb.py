from country import Country
from user import User
from note import Note
class Mydb():
  def __init__(self):
    print("hello")
    self.Country=Country()
    self.User=User()
    self.Note=Note()
