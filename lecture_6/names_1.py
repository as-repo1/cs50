name = input("what is your name: ")

file = open("names.txt", "a") #a if for append, and take consider the old inputs
file.write(f"{name}\n")
file.close()