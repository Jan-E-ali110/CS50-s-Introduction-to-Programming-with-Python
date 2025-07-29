user = input("Item: ")
items={
        "apple": 130, "Avocado": 50,"Kiwifruit": 90, "pear": 100,"Sweet Cherries": 100,
    }

for item in items:
    if item == user:
        print(f"Calories: {items[item]}")
        found = True
        break

