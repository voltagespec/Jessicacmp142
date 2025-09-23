class Student:
  def __init__(self, name, age):
     self.name = name
     self.age = age
  def introduction(self):
    return f"my anem is {self.name} and I am {self.age} years old"
student1 = Student("Jessie" 18)
print(student1.introduction())
  
