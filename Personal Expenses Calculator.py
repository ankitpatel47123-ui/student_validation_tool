# Student Monthly Budget Analyzer
name = input("Enter student name : ")
a = int(input("Enter monthly income : ₹"))
b = int(input("Enter monthaly rent : ₹"))
c = int(input("Enter monthaly food expenses : ₹"))
d = int(input("Enter monthaly travel expenses : ₹"))
e = int(input("Enter monthaly Mobile/internet expenses : ₹"))
f = int(input("Enter monthaly other expenses :₹"))
print("The program should calculate")
g = b+c+d+e+f
print(f"Total expenses :₹{g}")
h = a - g
print(f"Remaining mony :₹{h}")
i = (g/a)*100
print(f"Monhtaly expenses percentage :{i}%")
j = 100-i
print(f"Monthaly seving percentage :{j}%")