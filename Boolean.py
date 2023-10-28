#True/False
x = 2
print(x==2)
print(x==3)
print(x<3)
print(x>3)

#And/OR
name = "Boopesh"
age = 31
if name == "Boopesh" and age == 31:
    print("Your name is %s" % name)
    print("Your age is %d" % age)

#IN
lst = ["Boopesh", "Vikram", "Viyan", "Naveena"]
name = "Viyan"
if name in lst:
    print("it is in the list")
else:
    print("not in the list")

#IS
x = [1,2,3]
y=[1,2,3]
print (x==y)
print(x is y)

#NOT
print(not False)

#Change the variables in the first section, so that each if statement resolves as True.

number = 10
first_array = [1,2,3]
second_array = [1,2]
if number < 11:
    print("one")
if len(first_array) == 3:
    print("two")
if len(second_array) == 2:
    print("three")
if len(first_array) + len(second_array) ==5:
    print("four")
if first_array[1] == 2:
    print("five")
if second_array[0] ==1:
    print("six")



