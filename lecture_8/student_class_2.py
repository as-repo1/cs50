class Student:
    def __init__(self, name, house, patronus):#self gives us the access to the current object that was just created ,it stores them 'self'
        if not name:
            raise ValueError("Missing Name!!")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house!!")
        self.name = name
        self.house = house
        self.patronus = patronus
        
    def __str__(self):
        return f"{self.name} form {self.house}"
        
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐹"
            case "Otter":
               return "🐧"
            case "Jack":
                return "🕷️"
            case _:
                return "∰௹𑿠⛆"
        
def main():
    student = get_student()
    print("gili-gili-hocus_focus :)")
    print(student.charm())
    # print(f"{student.name} from {student.house}")
    # print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    student = Student(name, house, patronus)#constructor call
    return student

if __name__ == "__main__":
    main()