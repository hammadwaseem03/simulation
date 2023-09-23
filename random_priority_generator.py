import math

A = int(input("input the value of A for random priority generator"))
a = int(input("input the value of a for random priority generator"))
b = int(input("input the value of b for random priority generator"))
M = int(input("input the value of M for random priority generator"))
c = int(input("input the value of c for random priority generator"))
Z_not = int(input("input the value of Z for random priority generator"))
No_of_priority = int(input("enter the number of priority"))
Z = [Z_not]

R = []
random_number = []
Priority = []

for i in range(No_of_priority):
    Z_element = (A * Z[i] + c) % M
# the first element is Z_not
    Z.append(Z_element)
    # the first element is z[i+1]
    R.append(Z_element)

for i in range(No_of_priority):
    random_number_element = R[i] / M
    random_number.append(random_number_element)

for i in range(No_of_priority):
    Priority_element = (b - a) * random_number[i] + a
    Priority.append(round(Priority_element))

# Print header
print("\nPriority Values:")
print(f"{'Z':<10} | {'R':<10} | {'Random number':<20} | {'Priority':<10}\n")

# Print Z, R, Random number, and Priority values
for i in range(No_of_priority):
    print(f"{Z[i]:<10} | {R[i]:<10} | {random_number[i]:<20} | {Priority[i]:<10}")

# Add a separator line
print("\n------------------\n")
