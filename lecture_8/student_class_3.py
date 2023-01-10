class Student:
    # self gives us the access to the current object that was just created ,it stores them 'self'
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name!!")
        # if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
        #    raise ValueError("Invalid house!!")
        # those are comment out because, don't need then because we are usin the getter and setter function
        self.name = name    # instance variable
        self.house = house

    def __str__(self):
        return f"{self.name} form {self.house}"

    # Getter
    @property
    def house(self):
        return self._house 
    # we are using the _ thing bcs, we are using the 9,10th line , and those names are gonnal colide ,
    # be doing this we are differentiating them from each other , but still using them 
    
     
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
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)  # constructor call
    return student


if __name__ == "__main__":
    main()
