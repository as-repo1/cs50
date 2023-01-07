import re
url = input("URL: ").strip()

# username = url.replace("https://twitter.com/", "")
# print(f"Username: {username}")

# by using the regular expression 
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")
