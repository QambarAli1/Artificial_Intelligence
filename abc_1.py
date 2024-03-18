class Student:
    # name = "Qambar"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        # print("Constructor")
        # print(self)
        pass

    def getName(self):
        print(self.name)

    def getMarks(self):
        return self.marks
    
    @staticmethod #decorator
    def greet():
        print("Hello")


s1 = Student("Ali", 100)
print(s1.name, s1.marks)
s1.getName()
print(s1.getMarks())
s1.greet()