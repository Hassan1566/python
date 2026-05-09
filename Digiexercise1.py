# Program to calculate tax based on salary
salary = int(input('Enter the value of salary: '))       

if salary < 30000:
    tax_rate = 0.05
elif 30000 <= salary <= 70000:
    tax_rate = 0.15
else:
    tax_rate = 0.25

tax_amount = salary * tax_rate
net_salary = salary - tax_amount

print(f"Tax Amount: {tax_amount}")
print(f"Net Salary: {net_salary}")

# Convert the list into dictionary
fruit_list = ['apple', 'banana', 'kiwi', 'cherry', 'mango']
dict = dict(zip(fruit_list, range(1, 6)))
print(dict)

