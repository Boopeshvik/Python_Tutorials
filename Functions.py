def my_function():
    print("I love India")
my_function()

#Examples

#I want to sing the bday song 3 times , instead of using the same code thrice , I can define
#once in function and call the function 3 times.

def bday_song(name,age):
    print(f"Happy brithday to {name}")
    print(f"you are {age} old")
    print (f"may god bless you {name}")

bday_song("Vikram", 31)

bday_song("Viyan", 2)

def function_1 (name,bill,date):
    print(f"your name is {name} and your bill amount is ${bill} which is due on {date}")

function_1("Boopesh","65.78","28-10-2023")



