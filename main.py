print("This line will be printed.")

x = 1
if x == 1:
    # indented four spaces
    print("x is 7.")

print("Goodbye, World!")

myint=7
print(myint)

myfloat =7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

mystring = 'Bogdan'
print(mystring)
mystring = "Bogush"
print(mystring)

one = 1
two = 2
three = one + two
print(three)

hello = "Heloo"
bogdan = ' Bogdan!'
line = hello + bogdan
print(line)

a, b = 3, 5
print(a,b)

# change this code
mystring = "hello"
myfloat = 10.0
myint = 20
# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3
# prints out 1,2,3
for x in mylist:
    print(x)

mylist = [1,2,3]
print(mylist[0])

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]
# write your code here
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")
second_name = names[0]
# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

number = 1 + 17 * 3 / 8.0
print(number)

remainder = 16 % 3
print(remainder)

squared = 23 ** 2
cubed = 35 ** 3
print(squared)
print(cubed)

helloworld = "help" + " " + "world"
print(helloworld)

lotsofhellos = "Sasuke " * 3
print(lotsofhellos)

even_numbers = [1,2,3,4]
odd_numbers = [6,7,8,9]
all_numbers = even_numbers + odd_numbers
print(all_numbers)

print([1,2,3] * 3)

x = object()
y = object()
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list
print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))
# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

name = "Bogdan"
print("Hello, %s !" % name)

name = "Bogdan"
age = 19
print("%s is %d years old." % (name, age))

mylist = [15,9,2001]
print("Birthday: %s" % mylist)

data = ("Bogdan", "Marti", 79.47)
format_string = "Hello %s %s. Your current balance is $%s."
print(format_string % data)

astring = "Hello world!"
astring2 = 'Hello world!'

astring = "Hello world!"
print("single quotes are ' '")
print(len(astring))

astring = "Hello world!"
print(astring.index("o"))

astring = "Hello world!"
print(astring.count("l"))

astring = "Hello world!"
print(astring[3:7])

astring = "Hello world!"
print(astring[3:7:2])

astring = "Hello world!"
print(astring[3:7])
print(astring[3:7:1])

s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

print("The first occurrence of the letter a = %d" % s.index("a"))
print("a occurs %d times" % s.count("a"))
print("The first five characters are '%s'" % s[:5])
print("The next five characters are '%s'" % s[5:10])
print("The thirteenth character is '%s'" % s[12])
print("The characters with odd index are '%s'" %s[1::2])
print("The last five characters are '%s'" % s[-5:])
print("String in uppercase: %s" % s.upper())
print("String in lowercase: %s" % s.lower())
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")
print("Split the words of the string: %s" % s.split(" "))
