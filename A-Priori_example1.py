from itertools import combinations

transactions = [
    {"Bread", "Milk"},
    {"Bread", "Diaper", "Beer", "Eggs"},
    {"Milk", "Diaper", "Beer"},
    {"Bread", "Milk", "Diaper", "Beer"},
    {"Bread", "Milk", "Diaper"}
]

items = ["Bread", "Milk", "Diaper", "Beer", "Eggs"]

for i in range(1,3):
    comb = combinations(items,i)
    for c in comb:
        count = sum(1 for t in transactions if set(c).issubset(t))
        if count >= 2:
            print(c,"support:",count)