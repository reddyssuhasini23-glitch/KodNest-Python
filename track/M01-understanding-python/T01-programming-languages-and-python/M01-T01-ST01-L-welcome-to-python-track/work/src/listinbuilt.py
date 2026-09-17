l = [2, 3, 4, 5, 6, 7, "data"]
l.insert(4, "Python")
print(l)

l = [12, 1.8, 9, False, "data"]
l.pop()
print(l)
l.pop(2)
print(l)

l = [3, 12, 15, 20, 1.8, "hi"]
l.remove("hi")
print(l)

l = [1, 2, 3, 4]
l.extend([10, 9, 8, 7])
print(l)

l = [1, 2, 3, 4]
l.sort()
print(l)

l = [1, 2, 3, 4]
l.remove(2)
print(l)

l = [4, 3, 2, 1]
l.sort()
print(l)

l = [1, 2, 3, 1, 4, 5, 6]
print(l.count(1))

l = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(l.count(1, ))

l = [5, 3, 4, 2, 1]
print(l.index(3))
print(l.index(1))
print(l.index(5))




