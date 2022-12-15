from emoji import emojize

str = input("Input: ")
if ":" in str:
    start = str.index(":")
    if ":" in str[start:]:
        end = str.index(":",start+1)
        smiley = str[start:end+1]
        str = str.replace(smiley,emojize(smiley))
print(str)