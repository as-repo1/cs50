a = int(input("how many people are there ? "))

names = []

for _ in range (a):
    names.append(input("what is your name: "))
    
for name in names:
    print(f"hello, {name}")