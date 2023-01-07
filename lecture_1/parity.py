def main():
    x = int(input("give x: "))
    if is_even(x):
        print("even")
    else:
        print("odd")

def is_even(n):

#    if n % 2 == 0:
#        return True                     #way_1
#    else:
#        return False

#   return True if n%2==0 else False         #way_2

    return n%2==0                            #way_3

main()

