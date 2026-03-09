from itertools import combinations

orders = [
    {"Burger","Fries","Soda"},
    {"Burger","Fries"},
    {"Pizza","Soda"},
    {"Burger","Soda"},
    {"Burger","Fries","Soda"}
]

items = ["Burger","Fries","Soda","Pizza"]

for i in range(1,3):
    comb = combinations(items,i)
    for c in comb:
        count = sum(1 for o in orders if set(c).issubset(o))
        if count >= 2:
            print(c,"support:",count)