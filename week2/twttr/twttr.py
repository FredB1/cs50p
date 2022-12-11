vowels = ["a","e","i","o","u"]
val = input("Input: ")
temp = val
for i in range(len(val)):
    if val[i].lower() in vowels:
        temp = temp.replace(val[i],"")
print(f"Output: {temp}")