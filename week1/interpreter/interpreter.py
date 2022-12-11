exp =input("Expression: ")
exp = exp.split(" ")
x = float(exp[0])
y = float(exp[2])
if exp[1]=="+":
    print(x+y)
elif exp[1]=="-":
    print(x-y)
elif exp[1]=="*":
    print(x*y)
elif exp[1]=="/":
    print(f"{x/y:.1f}")