---------------------------------------------------------
a = "Harsh Gupta"
print(a[3])

Output -  s
--------------------------------------------------------
for x in "Harsh":
  print(x)

Output - 
H
a
r
s
h
----------------------------------------------------------
a = "Harsh Gupta"
print(len(a))

Output - 11
----------------------------------------------------------
txt = "Python is very easy language"
print("Python" in txt)

Output - True
-----------------------------------------------------------
txt = "Python is very easy language"
if "Python" in txt:
  print("Yes, 'Python' is present.")

Output - Yes, 'Python' is present.
------------------------------------------------------------
b = "Harsh Gupta"
print(b[:5])

Output - Harsh
------------------------------------------------------------
a = "Harsh Gupta"
print(a[-5:-1])

Output - Gupt
-------------------------------------------------------------
txt = "Harsh Gupta"
print(txt.upper())   
print(txt.lower())   

Output - 
HARSH GUPTA
harsh gupta
-------------------------------------------------------------
txt = "apple,banana,mango"
print(txt.split(","))

Output - ['apple', 'banana', 'mango']
--------------------------------------------------------------
txt = "   hello harsh                "
print(txt.strip())

Output - hello harsh
--------------------------------------------------------------
first_name = "Harsh"
last_name = "Gupta"
full_name = first_name + " " + last_name
print(full_name)

Output - Harsh Gupta
---------------------------------------------------------------
name = "Harsh"
age = 21
print(f"My name is {name} and I am {age} years old.")

Output - My name is Harsh and I am 21 years old.
----------------------------------------------------------------
price = 50
quantity = 2
print(f"Total price is {price * quantity}")

Output - Total price is 100
-----------------------------------------------------------------
name = "Harsh"
age = 21
print("My name is {} and I am {} years old".format(name, age))

Output - My name is Harsh and I am 21 years old
------------------------------------------------------------------
print("Hello\nHarsh")         
print("Hello\tGupta")          
print("My name is \"Harsh\"")  
print('It\'s Python')          
print("C:\\Users\\Harsh") 

Output - 
Hello
Harsh
Hello    Gupta
My name is "Harsh"
It's Python
C:\Users\Harsh
--------------------------------------------------------------------
name = "Harsh gupta"
print(name.find("gupta"))

Output - 6
-------------------------------------------------------------------
fruit = "apple apple mango"
print(fruit.count("apple"))

Output - 2
--------------------------------------------------------------------
a = "hello world"
print(a.capitalize())

Output - Hello world
--------------------------------------------------------------------
name = "Harsh Gupta"
print(name.startswith("Harsh"))

Output - True
--------------------------------------------------------------------
name = "Harsh Gupta"
print(name.endswith("Gupta"))

Output - True
---------------------------------------------------------------------
name = "Harsh Gupta"
print(name.swapcase())

Output - hARSH gUPTA
---------------------------------------------------------------------
name = ["Harsh", "Gupta"]
print(" ".join(name))

Output - Harsh Gupta
----------------------------------------------------------------------
txt = "hello world"
print(txt.title())

Output - Hello World
----------------------------------------------------------------------
txt = "Harsh"
print(txt.center(20))

Output -        Harsh
-----------------------------------------------------------------------
data = {"name": "Harsh"}
print("My name is {name}".format_map(data))

Output - My name is Harsh
-----------------------------------------------------------------------
txt = "Hello World"
print(txt.index("World"))

Output - 6
------------------------------------------------------------------------
txt = "Harsh123"
print(txt.isalnum())

Output - True
------------------------------------------------------------------------
txt = "Harsh123"
print(txt.isalpha())

Output - False
------------------------------------------------------------------------
txt = "123"
print(txt.isdecimal())

Output - True
------------------------------------------------------------------------
txt = "my_var"
print(txt.isidentifier())

Output - True
-------------------------------------------------------------------------
txt = "hello world hello"
print(txt.rfind("hello"))

Output - 12
-------------------------------------------------------------------------
