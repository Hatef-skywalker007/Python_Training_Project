class Student:

    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores

    def get_average(self):
        return sum(self.scores) / len(self.scores)

    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Average:", self.get_average())


student = Student(
    "Ali",
    20,
    [15, 18, 17, 20]
)

student.show_info()
#Class + Object + List + Function + Method