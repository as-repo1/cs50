def main():
    name = input("give name: ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()

# *in py, we have to define the function first so that we can use that for letter  
# we can't define the function after calling it ,
# in that case we can def the main() so that we can use that , like that code , upd