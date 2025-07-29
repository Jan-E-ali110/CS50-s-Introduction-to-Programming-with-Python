vowels = "aeiou"
cap_vowels = "AEIOU"
user = input("Input: ")
for vow in vowels:
    user = user.replace(vow,"")
    for cap in cap_vowels:
        user = user.replace(cap,"")


print(f"Output: {user}")
