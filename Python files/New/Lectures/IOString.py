class IOString:
  def __init__(self):
    self.str1 = ""
  def get_String(self):
    self.str1 = input()
  def return_String(self):
    return(self.str1.upper())
str1 = IOString()
str1.get_String()
str1.return_String()

