# n = int(input("enter how many bricks you want: "))
# for _ in range(n):
#    print("#")

def main():
    n = int(input("enter how many bricks you want: "))
    print_column(n)
   

def print_column(height):
    for _ in range(height):
        print("#")


main()
