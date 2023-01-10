def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] == "Ravenclaw"
    
    print(f"{student['name']} from {student['house']}")
    
    # if student[0] == "Padma":  # return [name, house] not in '()'
    #    student[1] == "Ravenclaw"
    # print(f"{student[0]} is from {student[1]}")
    # print(f"{name} form {house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}
    
    
    # name = input("name: ")
    # house = input("house: ")
    # return [name, house]  # if in '()' then we can't change the value


if __name__ == "__main__":
    main()
