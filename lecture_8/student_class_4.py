class Student:
    # self gives us the access to the current object that was just created ,it stores them 'self'
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name!!")

        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} form {self.house}"

    @classmethod
    def get(cls):
        name = input("What is your name: ")
        house = input("What is your house: ")
        return cls(name, house)

    # Getter
    @property
    def house(self):
        return self._house

    # Setter

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house dude!")
        self._house = house

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Enter the name dude!!")


def main():
    # student = get_student()
    student = Student.get()
    print(student)


# def get_student():
#    name = input("Name: ")
#    house = input("House: ")
#    student = Student(name, house)  # constructor call
#    return student


if __name__ == "__main__":
    main()
