set1 = {"a", "b", "c"}
set2 = {1, 2, 3, "b"}

for x in set1:
    print(x)

print(set1.union(set2))

print(set1.intersection(set2))

print(set1.difference(set2))