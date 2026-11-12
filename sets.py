s = {1, 2, 3, 3, 2}
print(s)
print(len(s))



marks = [80, 90, 80, 70, 90]
unique = set(marks)
print(unique)
print(list(unique))
print(set("banana"))

emails = ["a@x.com", "b@x.com", "a@x.com"]
print(len(set(emails)))


s = {"red", "green"}
s.add("blue")
print(s)
s.update(["pink", "black"])
print(s)
s.remove("green")
print(s)
s.discard("white")
print(s)
x = s.pop()
print(x)
s.clear()


s = {10, 20, 30}
print(20 in s)
print(40 in s)
print(len(s),max(s),min(s),sum(s))


python_class = {"Anu", "Ben", "Cia", "Dev"}
java_class = {"Cia", "Dev", "Eli", "Fay"}

print(python_class | java_class)
print(python_class.union(java_class))
print(len(python_class | java_class))


print(python_class & java_class)
print(python_class.intersection(java_class))

print(python_class - java_class)
print(java_class - python_class)

print(python_class ^ java_class)
print(python_class .symmetric_difference(java_class))

a = {1,2}
b = {1,2,3,4}
print(a.issubset(b))
print(a.issuperset(a))
print(a.isdisjoint({5, 6}))
print(a.isdisjoint(b))