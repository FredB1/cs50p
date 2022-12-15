from sys import exit
def main():
    word =(input("Input: "))
    word = shorten(word)
    print(f"Output: {word}")
    exit(0)
def shorten(word):
    vowels = ["a","e","i","o","u", "A","E","I","O","U"]
    length = len(word)
    while length > 0:
        if word[length-1]in vowels:
            word = word.replace(word[length-1],"")
            length -= 1
        length -= 1
    return word

if __name__ == "__main__":
    main()