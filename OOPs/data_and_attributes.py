class Employee:
  def __init__(self):
    print("initialization starting")
    self.id = 123
    self.salary = 50000
    self.location = "pune"
    print("initialization done")

  def travel(self, destination):
    print("travel method called manually")
    print("employee has gone to the",destination)

sam = Employee()
# print(sam.id)
# sam.travel("kerala")

print(type(sam))

from oop_proj import chatbook
user=chatbook()