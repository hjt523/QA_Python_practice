

class students:
    def __init__(self,name, age, studentclass):
        self.name = name
        self.age = age
        self.studentclass = studentclass

    def scoreavg(self,Test1,Test2,Test3):
        avg = (Test1 + Test2 + Test3) / 3
        return avg


Ben = students("Ben", 12, '1A')
print ("Students Name: ", Ben.name)
print ("Students Age: ", Ben.age)
print ("Students class: ",Ben.studentclass )
print (Ben.scoreavg(12,6,9))


#example
'''

class Dog:
    energy = "high"

    def speak(self):
        print("woof")

bilbo_waggins = Dog()
print(bilbo_waggins.energy)
bilbo_waggins.speak()
'''