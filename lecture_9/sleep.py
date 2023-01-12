def main():
    n    = int(input("What's n? "))
    for s in sheep(n):
       print(s)


def sheep(n):
    flock = []
    for i in range(n):
    #    flock.append("🐑"*i)
    #return flock
        yield "🐑" * i  #yield is an eterator


if __name__ == "__main__":
    main()