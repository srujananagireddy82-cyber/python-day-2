"""
an operators is a special symbol
which is used to perform an operation
ex:c=a+b
here c,a,b are operands
+ is a special symbol

the python operators are:
1.arthimetic operator
2.relational operator
3.logical operator
4.bitwise operator
5.identity operator
6.membership operator
7.assignment operator
"""

"""
1.arthimetic operator:
it is used to perform some mathematical
or arthimetic operation
the operators are +,-,,/,//,%,*
NOTE:input() is a function which takes input from user
"""
#code
a=int(input("enter a number:"))
b=int(input("enter a number:"))
print("the addition",a+b)
print("the subtraction",a-b)
print("the multiplication",a*b)
print("the division",a*b)
print("the floordivision",a//b)
print("the modular division",a%b)
print("the power",a**b)

"""
2.relational operators:
these are used to compare the values
and return the boolen they are
>,<,>=,<=,==,!=
"""
#code
a=int(input("enter a number:"))
b=int(input("enter a number:"))
print("the greater value",a>b)
print("the lesser value",a<b)
print("the greater than or equals too value",a>=b)
print("the less than or equals too value",a<=b)
print("equals too value",a==b)
print("the not equals too value",a!=b)

"""
3.logical operators:
these are used to perform logical operations
there are logical and,or,not
and--if both the conditions are True it returns the True
T T T
F T F
T F F
F F F
or--if one of the condition is True it returns the True
T F T
F T T
T T T 
F F F 
not--if just negotiates the condition
T F
F T 
"""
#code
a=13
b=45
c=a>=34 and b<=50
print(c)
d=67
e=89
f=d!=67 or e==89
print(f)
g=10
print(not(g))
h=0
print(not(h))

"""
4.bitwise operators:
these are used to perform binay operatins
they are
bitwise and(&):if both the bits are "1" it returns "1"
bitwise or(!):if one of the bit is "1" it returns "1"
bitwise xor(^):if one of the bit is "1" it returns "1"
and if both the bits are "1" it returns "0"
"""
#code
a=5 
b=9
c=a&b
print(c)
d=15
e=13
f=d/e
print(f)
g=12
h=14
i=g^h
print(i)

"""
5.membership operators:
these are used to check the values in a sequence
and returns the boolean values 
they operators are "in","not in"
"""
#code
x=["apple","banana"]
print("apple"in x)
print("pp"not in x)
print("banana"not in x)
print("dragon"in x)

"""
6.identity operators:
there are used to comapere the values 
and returns the boolean values
the operators are "is","is not"
"""
#code
x=[1,2,3]
y=[4,5,6]
z=[4,5,6]
x=y=z
print(x is y)
print(x is z )
print(y is z)
print(y is not z)
print(z is not y)
print(x is not y)
#7)membership operator :
#memmber ship operatoer is used yo check the values in a sequence and returns the boolean values 
#program
x=["apple""banana"]
print("apple"in x)
print("pp"not in x)
print("banana"not in x)
print("dragon"in x)
