class Person:
    def __init__(self, name):
        self._name = name

    def get_info(self):
        return f"Person name: {self._name}"


class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def get_info(self):
        return f"Student name: {self._name}, ID: {self.student_id}"


p = Person("Mans")
s = Student("Mansur", 101)

print(p.get_info())
print(s.get_info())
