def main():
    x = get_int()
    print(f"value of x is: {x}") #we have to use the 'f' here!

def get_int(): 
    while True:
        try: #exception handling
            x = int(input("what is the value of X: "))
        except ValueError:
            print("x is not an integer")
        else:
            return x
    

main()