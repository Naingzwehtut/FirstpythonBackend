# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# p1 = Person("john",22)
# print(p1.name)

from inheritance import Student

class Person(Student):
    pass

p1 = Person()
print(p1.name)