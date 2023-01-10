class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Name!!")


class Student(Wizard):
    def __init__(self, name, house):
       # if not name:
       #     raise ValueError("Missing Name!!")
       # self.name = name
        super().__init__(name)
        self.house = house

    ...

class Professor(Wizard):
    def __init__(self, name, subject):
        # if not name:
        #    raise ValueError("Missing Name!!")
       # self.name = name
        super().__init__(name)
        self.subject = subject


wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defecse Againt the Dark Arts")