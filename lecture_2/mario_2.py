def main():
    size = int(input("enter the size of the brick to print: "))
    print_square(size)


def print_square(size):
    for i in range(size):
        print_row(size)


def print_row(width):
    print("# " * width)   #string multiplication tecnique


main()
