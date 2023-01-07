name = input("what's your name dude: ").strip().title()

#splits the user's name into first and second name
first, last = name.split(" ")

print(f"hello, {first}") #printing only the first name here