from sys import exit
def main():
    str = value(input("Greeting:"))
    print(f"${str}")
    exit(0)
def value(greeting):
    greeting = greeting.lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        print(greeting)
        return 100


if __name__ == "__main__":
    main()