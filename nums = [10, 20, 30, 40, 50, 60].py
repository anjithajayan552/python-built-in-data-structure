scores = [45, 90, 67, 90, 30]
print(scores.count(90))
print(scores.index(67))
print(90 in scores)
print(max(scores),min(scores))
print(sum(scores)/len(scores))
print(sorted(scores))
scores.sort(reverse = True)
print(scores) 






a = [1, 2, 3]
b = a
b.append(4)
print(a)
c = a.copy()
c.append(5)
print(a, c)
print([1,2] + [3] ,[0]*3)
