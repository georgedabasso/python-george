#python comments-this is a single line comment
"""
this is a simple multiline comment in python
"""

#variables
student_name = "Jonathan" #data type is string
student_age = 25 #integer
student_fee = 100.0 #float
student_marks = 100 #integer
is_male = True #boolean

#outputting values in variables
print(student_name, student_age, student_fee)
print(student_age)
print(is_male)



student_name = "Jonathan"
student_name = "Allan"
print(student_name)


#case sensitivity
STUDENT_NAME = "Ryan"
student_name = "Ben"
print(STUDENT_NAME)


#variable naming in python
book_price=20.0 #valid variable name
_book_price=20.0 #valid variable name



x=y=z=10 #assigning one value to multiple variables
x,y,z= 30, 40, 50 #multiple values being assigned multiple variables

price= 10
qty= 4
total_price= price*qty
print("the total price is: " +str(total_price)+ "Kenyan shillings")

firstname= "Jonathan"
secondname= "Kimani"
thirdname= firstname*4
print("my thirdname is :" ,thirdname,)

#logical operator
constituency= "embakasi"

if constituency=="embakasi" or "westlands" or "kasarani":
    print("can be governor")
else:
    print("cannot be governor")


