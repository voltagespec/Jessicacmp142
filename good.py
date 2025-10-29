# I like the comments. But where is your project idea file???
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



  class Student:
    def __init__(self, name, age, student_id):
        # Public attribute
        self.name = name
        
        # Protected attribute (accessible in subclasses)
        self._age = age
        
        # Private attribute (not directly accessible outside class)
        self.__student_id = student_id

    # Public method
    def display_info(self):
        print(f"Name: {self.name}, Age: {self._age}")

    # Protected method
    def _get_age(self):
        return self._age

    # Private method
    def __get_student_id(self):
        return self.__student_id

    # Public method to access private data safely (encapsulation)
    def get_student_id(self):
        return self.__get_student_id()


# Child class 1
class Undergraduate(Student):
    def __init__(self, name, age, student_id, major):
        super().__init__(name, age, student_id)
        self.major = major

    def display_undergrad(self):
        print(f"Undergraduate Student: {self.name}, Major: {self.major}")
        print(f"Age (protected): {self._get_age()}")
        print(f"Student ID (via encapsulated method): {self.get_student_id()}")


# Child class 2
class Graduate(Student):
    def __init__(self, name, age, student_id, research_topic):
        super().__init__(name, age, student_id)
        self.research_topic = research_topic

    def display_graduate(self):
        print(f"Graduate Student: {self.name}, Research Topic: {self.research_topic}")
        print(f"Age (protected): {self._get_age()}")
        print(f"Student ID (via encapsulated method): {self.get_student_id()}")


u1 = Undergraduate("Alice", 20, "U123", "Computer Science")
u1.display_undergrad()

print("\n")

g1 = Graduate("Bob", 25, "G456", "Artificial Intelligence")
g1.display_graduate()

