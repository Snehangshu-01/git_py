a = int(input("This is: "))
b = int(input("That is: "))
c = int(input("and this is: "))

root1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
root2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)

print(root1)
print(root2)
