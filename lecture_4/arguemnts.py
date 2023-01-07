import sys

if len(sys.argv) < 2:
    sys.exit("too few arguments!")
elif len(sys.argv) > 2:
    sys.exit("too many argumets!")
 
print("hello, the file name is: ", sys.argv[0])
print("hello, my name is: ", sys.argv[1])