item_dict = {}
while True:
    try:
        item = input().upper()
        item_dict[item] = item_dict.get(item, 0) + 1

    except EOFError:
        break

item_dict = dict(sorted(item_dict.items()))
for item in item_dict:
    print(item_dict[item] , item)

