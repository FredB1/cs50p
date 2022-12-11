def main():
    mess = input("")
    print(convert(mess))
def convert(x):
    x= x.replace(":)","🙂")
    x=  x.replace(":(","🙁")
    return x

main()