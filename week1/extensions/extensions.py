val = input("File name: ").strip().lower()
if val.endswith(".gif"):
    print("image/gif")
elif val.endswith(".jpg") or val.endswith(".jpeg"):
    print("image/jpeg")
elif val.endswith(".png"):
    print("image/png")
elif val.endswith(".pdf"):
    print("application/pdf")
elif val.endswith(".txt"):
    print("text/plain")
elif val.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")