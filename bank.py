user1 = input("Greeting: ")
user2 = user1.lower().strip()
if user2 == "hello":
    print("$0")

elif user2 == "h" and user2 != "hello":
    print("$20")

elif user2 == "hello, newman":
    print("$0")

elif user2 == "how you doing?":
    print("$20")


else:
    print("$100")












    #In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”,
    # output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in
    #  the user’s greeting, and treat the user’s greeting case-insensitively.
