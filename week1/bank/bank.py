val = input("Greeting:").strip().lower()
if val.startswith("hello"):
    print("$0")
elif val.startswith("h"):
    print("$20")
else:
    print("$100")