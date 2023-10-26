#Add , Sub, Multiply , Division

x = 10
y = 20
z = (y-x)*10/10
print (z)

#modolo operator %

remainder = 11 % 3
print(remainder)

#Power Symbol

square = 7**2
cube = 2**3
print (square)
print (cube)

# String Addition

string = "hello" + " " + "world"
print(string)

# String multiplication

string_multiply = "Viyan" * 5
print(string_multiply)

# Operators with Lists

a = [1,2,3,4]
b = [5,6,7,8]
c = a + b
print (c)

#The target of this exercise is to create two lists called x_list and y_list, which contain 10 instances of the variables x and y, respectively. You are also required to create a list called big_list, which contains the variables x and y, 10 times each, by concatenating the two lists you have created.

x_list = [x] *10
y_list = [y] *10
big_list = x_list + y_list

print("x list contains %s objects" % len(x_list) )
print("y list contains %s objects" % len(y_list))
print("biglist contains %d objects" % len(big_list))
