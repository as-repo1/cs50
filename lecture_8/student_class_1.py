class Student:
    def __init__(self, name, house):#self gives us the access to the current object that was just created ,it stores them 'self'
        if not name:
            raise ValueError("Missing Name!!")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house!!")
        self.name = name
        self.house = house
        
        #2 def __str__(self):
            #2 return f"{self.name} form {self.house}"
        
def main():
    student = get_student()
    #1 print(f"{student.name} from {student.house}")
    #2 print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)#constructor call
    
    #1 student = Student()
    #1 student.name = input("Name: ")
    #1 student.house = input("House: ")
    return student


if __name__ == "__main__":
    main()
