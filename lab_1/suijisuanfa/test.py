list1 = [1, 3, 65, 2, 7]
list2 = [3, 2, 5, 4]

c = [x for x in list1 if x in list2]
d = [y for y in (list1 + list2) if y not in c]

print(c)
print(d)


print(list1.index(46))

