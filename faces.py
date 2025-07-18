def main():
    txt = input()
    print(convert(txt))

def convert(txt):
    return txt.replace(":)","🙂").replace(":(","🙁")

main()
