val = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip().replace(" ", "")
if val == "42" or val == "forty-two" or val.lower()=="forty-two" or val.lower()=="fortytwo":
    print("Yes")
else:
    print("No")