class Student():
  def __init__(self,_name,_sid, _GPAperyears):
    self.name = _name
    self.sid = _sid
    self.GPAperyears = _GPAperyears

  def getTotalGPA(self):
    TotalGPA=self.GPAperyears /len(self.GPAperyears )
