balance = 0


def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)


def deposit(n):
    global balance  # for changing the values of the balance which is a global variable
    balance += n


def withdraw(n):
    withdraw -= n


if __name__ == "__main__":
    main()
