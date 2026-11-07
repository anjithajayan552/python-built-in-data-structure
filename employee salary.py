emp_name = input("Enter employee name:")
emp_id = input("enter employee id:")
basic_salary =input("enter basic salary:")
HRA = input("enter HRA:")
travel_allowance = input("enter travel allowance:")
PF = input("enter PF deduction :")

basic_salary = float(basic_salary)
HRA = float(HRA)
travel_allowance = float(travel_allowance)
PF = float(PF)

total_allowance = HRA + travel_allowance
gross_salary = basic_salary + total_allowance
net_salary = gross_salary - PF

print("Employee name :", emp_name)
print("employee id :", emp_id)
print("PF deduction :", PF)
print("gross salary:", gross_salary)
print("net salary:", net_salary)