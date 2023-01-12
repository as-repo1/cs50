def main():
    yell("This", "is", "CS50")


def yell(*words):
    # uppercased = [] # list ,list(),can be used
    # for word in words:
    #    uppercased.append(word.upper())
    
    #uppercased = map(str.upper, words)
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__main__":
    main()
