import re

email = input("what is your edu email: ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE): #\w for [a-zA-Z0-9_ ]
    print("Valid")
else: print("Invalid")




# username, domain = email.split("@")#

# if username:
#    print("valid")
# else:
#    print("Invalied")
