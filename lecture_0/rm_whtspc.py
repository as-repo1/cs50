name = input("what's your name dude: ")

#removal of white space in python
name = name.strip()

#capitalize user's name
name = name.capitalize() #only the first word

#for all words
name = name.title()

print(f"hello, {name}")