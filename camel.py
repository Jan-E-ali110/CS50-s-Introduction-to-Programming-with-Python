camelcase = input("CamelCase: ")

for camel in camelcase:
    if camel.isupper():
        print("_",end="")
    print(camel.lower(), end="")

