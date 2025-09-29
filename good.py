class Student:
  def __init__(self, name, age):
     self.name = name
     self.age = age
  def introduction(self):
    return f"my anem is {self.name} and I am {self.age} years old"
student1 = Student("Jessie" 18)
print(student1.introduction()) 

#Good approach because it uses proper class structure costructor and method


class Student: 
  def details(self,name, age):
  return f"my name is {name} and i am {age} years old"
student1 = Sudent()
print(student1.details("jessie" 18))

#Bad approach. it worlds but doesnt follow proper oop principles. it doesnt store name and age inside the object.


class Student:
  pass
student1 = Student()
student1.name = "Jessie"
student1.age = 18
print("my name is" student1.name "and i am" student1.age "years old")


#Ugly approach because it doest have a proper structure. the class is empty.


#Define the functions(with explanation)
#Good appraoch - (__init__ and Introducton)
#_init_: is a cintructor and it initialiezes object attributes
#introduction(): is a method that uses object data to return a formatted message

#Bad approach - Details
#Details(name,age): is a method that returns student info but doesnt properlt bind the attributes to the object

#Ugly approach - (pass)
#theres no real function inside thr class. Data is directly attached outside so the class does nothing

  
