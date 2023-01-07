import sys

if len(sys.argv) < 2:
    sys.exit("too few arguments!")
for arguments in sys.argv[0:]:#with the name tag
    print("hello, my name is: ",arguments)
    
for arguments in sys.argv[1:]:#without the name tag
    print("\nhello, my name is: ",arguments)