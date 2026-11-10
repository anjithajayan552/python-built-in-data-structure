items = ["milk", "eggs", "rice", "eggs"]
print(items)
print(len(items))
print(type(items))


fruits = ["apple", "banana", "mango", "grape", "kiwi"]
print(fruits[0])
print(fruits[3])
print(fruits[-1])
print(fruits[-2])
print(fruits[2])



nums = [10, 20, 30, 40, 50, 60]
print(nums[1:4])
print(nums[:3])
print(nums[3:])
print(nums[::2])
print(nums[::-1])


colors = ["red", "green", "blue"]
colors[1] = "yellow"
print(colors)
colors[0:2]
print(colors)


cart = ["pen", "book"]
cart.append("bag")
print(cart)
cart.insert(1, "pencil")
print(cart)
cart.extend(["eraser", "sharpner"])
print(cart)



t = ["a", "b", "c","b", "d"]
print(t)
t.remove("b")
print(t)
x = t.pop()
print(x,t)
t.pop(0)
del t[0]
t.clear()
print(t)


scores = [45, 90, 67, 90, 30]
print(scores.count(90))
print(scores.index(67))
print(90 in scores)
print(max(scores), min(scores))
print(sum(scores)/len(scores))
print(sorted(scores))
scores.sort(reverse=True)
print(scores)



a = [1, 2, 3]
b= a
b.append(4)
print(a)
c= a.copy()
c.append(5)
print(a, c)
print([1, 2] + [3], [0] * 3)



