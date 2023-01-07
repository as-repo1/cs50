# name = input("What's your name ? ").strip()
# if "," in name:
#    last, first = name.split(", ")
#    # for those who have written their names reverse order by putting "," in btn
#    name = f"{first} {last}"
# print(f"hello", {name})


# by using regular expression
import re

name = input("what is your name dude ? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) +" "+ matches.group(1)
print(f"hello, {name}")