a = [1, 2, 2, 3, 3, 3, 4]
unique = set(a)
print(unique)

a = {}
print(type(a))
b =()
print(type(b))
class1 = {"anu", "binu","cathy","david"}
class2 = {"binu", "cathy", "eva", "john"}
bothclasses = class1 and class2
print(bothclasses)


python = {"Anu", "Binu", "Cathy", "David"}
java = {"Binu", "Cathy", "Eva", "John"}
python_only = python - java
print(python_only)


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a|b)
print(a and b)
print(a-b)
print(b - a)
print(a^b)


candidate_skills = {"HTML", "CSS", "Python", "Java"}
required_skills = {"HTML", "CSS"}
print(required_skills.issubset(candidate_skills))


friend1 = {"premam", "premalu", "hridayam","charlie"}
friend2 = {"premam", "manjimmalboys", "drishyam","charlie"}
print(friend1  & friend2)