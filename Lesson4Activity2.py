class student:
    name = "Jeb"
    grade = 10

    def introduction(self):
        print("Hi i am a student")

    def details(self):
        print("My name is", self.name)
        print("I am a", self.grade, "grader")

ob = student()
ob.introduction()
ob.details()