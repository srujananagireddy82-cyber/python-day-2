#python data types
#2)sequence
#in sequence there are 3 types
#a)list 
#b)tuple
#c)string
#a)list: is a collection of items \values it can be represented in[] and seperated by(,)list values are called as CVS(values comma sepereted values)
#program
#syntax:list name=[val1,val2,val3,]
# program
mylist=[17,9,1,17+9j, [1,2,3] ]
print(mylist)
print(type(mylist))
print(mylist[0])#17
print(mylist[3])#17+9j
print(mylist[4])#[123]
#how can change the elements in list using index
# index start with zero ends with n-1
#changing the elements in a list
# in elements are not accepting sring ex:"ece" in elements\values
#list is a mutable we can change the element
mylist[1]="srujana"
mylist[2]="introvert"
print(mylist)

#b)tuple:it is a collection of items\values elements 
#syntax:(vall,vall2,val3...valn)
#we can access the elements in a touple using index
#touple is immutable_unchangeble
#program
mytuple=(12,23.45,56+78j,5,7,8,9,(5,4),[67])#elements\values
print(mytuple)
print(type(mytuple))
print(mytuple[0])#12
print(mytuple[2])#56+78j
print(mytuple[7])#(5,4)
# in elements are not accepting sring ex:"ece" in elements\values
#it is immutable so touple elements doesn't change
#mylist[7]=17
#print(mytuple)# output  is not changed

#c)string:string is a collection of elements 
# it can be enclosed
#  within double quotes or single quotes(""),(' ')
string=("ece","srujana","prasad" ,"gayathri","durga" ,"we are family")
print(string)
print(type(string))
print(string[2])#prasad
print(string[4])#durga
print(string[3])#gayathri
print(string[1])#srujana
print(string[5])#we are family








