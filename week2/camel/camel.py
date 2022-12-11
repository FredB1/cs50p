val = input("camelCase: ")
for c in range(len(val)):
    if val[c].isupper():
        val=val.replace(val[c],"_"+val[c].lower())  
print(f"snake_case: {val}")