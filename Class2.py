class student:
    grade = 9
    name = "John"

    def intro(self):
        print("Hi I am a student")

    def det(self):
        print("My name is", self.name)
        print("I am in grade", self.grade)
ob= student()
ob.intro()
ob.det()