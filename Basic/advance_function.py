Function names and some basic info 

1.The index() function in a list is used to find the index (position) of a given value. You need to provide a value as an argument to the index() function, and it returns the index of the first occurrence of that value in the list.

2.
3.
4.
5.
6.
7.
8.
9.
10.

----------------------------------------------------------------------------------------------------

#QUE --- RETURN THE INDEX WHEN WE ENTER THE ELEMENT INTO index()?

mywords --- we need to enter the value as the parameters to the function then it will give us the index at which the element is lying. OUTPUT = INDEX.


#index() Returns the index of the element entered and only gives index of the original / first element occurrence and not duplicate

fruits = ['apple', 'banana', 'cherry','mango','cherry']

x = fruits.index("cherry") 

print(x)

print("THE INDEX AT WHICH CHERRY IS LOCATED IS :\t"fruits.index("cherry"))

output --- 2
index() Method for Lists
The index() method is used to find the index (position) of the first occurrence of a specified element in a list.

Syntax:
python
Copy code
list.index(element, start, end)
Parameters:
element (required): The element to search for in the list.
start (optional): The position in the list where the search starts. The default is 0, which means it starts from the beginning of the list.
end (optional): The position in the list where the search ends. The default is the length of the list, meaning it searches till the end of the list.
Return Value:
Returns the index (an integer) of the first occurrence of the specified element.
Raises a ValueError if the specified element is not found in the list.
Example:
python
Copy code
# Example list
fruits = ['apple', 'banana', 'cherry', 'banana', 'date']

# Find the index of the first occurrence of 'banana'
index = fruits.index('banana')
print(index)  # Output: 1
Using start and end Parameters:
You can also specify the range in which to search for the element by providing start and end parameters.

python
Copy code
# Example list
numbers = [10, 20, 30, 20, 40, 50]

# Find the index of the first occurrence of '20' starting from index 2
index = numbers.index(20, 2)
print(index)  # Output: 3

# Find the index of the first occurrence of '30' between indices 1 and 4
index = numbers.index(30, 1, 4)
print(index)  # Output: 2
Important Notes:
If the element appears multiple times in the list, index() will return the index of the first occurrence.
The search is case-sensitive if the list contains strings.
If the element is not found, a ValueError is raised.
Example with ValueError:
python
Copy code
# Example list
colors = ['red', 'green', 'blue']

# Trying to find an element that is not in the list
index = colors.index('yellow')  # Raises ValueError: 'yellow' is not in list
Would you like to know more about how to handle the ValueError or any other use cases for index() with lists?

----------------------------------------------------------------------------------------------------

#QUE -- INSERT elements at given index using insert(),and also explain the indexing changes happened due to 

	use of insert()??

#insert()	Adds an element at the specified POSITION / INDEX and the changes are made to the original 
		""list"",and there is no
 			
		duplication of list / no duplicate list is create. 

#shifting of index takes place automatically.
can enter anywhere within the list. 
And also support negative indexing.

fruits = ['apple', 'banana', 'cherry']

# 	fruits[0]="apple"  , fruits[1]="banana" , fruits[2]="cherry"

fruits = ['apple', 'banana', 'cherry']

fruits.insert(0,"orange") 

print(fruits,"\n")

print("THE CHANGE IN INDEX OF ELEMENT = 'APPLE' : =\t",fruits.index("apple"))

OUTPUT ---- 	['orange', 'apple', 'banana', 'cherry'] 
   	 	
		THE CHANGE IN INDEX OF ELEMENT = 'APPLE' : =	 1

----------------------------------------------------------------------------------------------------

#QUE -- POP THE ELEMENT FROM LIST USING POP()?

#pop()	Removes the element at the specified position,AND if position not specified removes the last element.

	fruits = ['apple', 'banana', 'cherry']

#here fruits[0]='apple'

fruits.pop(0) 

print(fruits) 		#output ---['banana', 'cherry']

print(fruits.index('banana'))  #OUTPUT --- NOW "BANANA WILL BE ON THE "0" INDEX ".

print(fruit.pop()) #OUTPUT === "cherry"

----------------------------------------------------------------------------------------------------

#QUE ---REMOVE A SPECIFIC ELEMENT WITH REMOVE() WHICH TAKES ELEMENT AS A PARAMETER.

remove()--Removes the first item with the specified value.And only take one argument at a time.

fruits = ['apple', 'banana', 'cherry']

fruits.remove("banana") 

print(fruits)

#OUTPUT ----	['apple', 'cherry']

----------------------------------------------------------------------------------------------------

#QUE -- REMOVE A SPECIFIC ELEMENT AND A WHOLE LIST USING DEL() ---DELETE FUNCTION.

thislist = ["apple", "banana", "cherry"]

del thislist[0]

print(thislist) 

#del whole list

thislist = ["apple", "banana", "cherry"]

del thislist   #---here we shall get error,cause the list gets DELETED at the 2 statement only

print(thislist) 

OUTPUT -----

Traceback (most recent call last):
  File "/home/admin123/basics/plang/2adv_dataypes/working.py", line 3, in <module>
    print(thislist)
NameError: name 'thislist' is not defined

----------------------------------------------------------------------------------------------------

#QUE --- REVERSE THE list using reverse()

#reverse()	Reverses the order of the list

fruits = ['apple', 'banana', 'cherry']

print(fruits)

print("BEFORE REVERSE := \t",fruits.index('cherry'))

fruits.reverse()

print(fruits) 

print("AFTER REVERSE := \t",fruits.index('cherry'))

OUTPUT----	['apple', 'banana', 'cherry']
		BEFORE REVERSE := 	 2
		['cherry', 'banana', 'apple']
		AFTER REVERSE := 	 0

----------------------------------------------------------------------------------------------------

#QUE --- SORT THE LIST 
"""
#sort()	Sorts the list

1.The sort() method sorts the list ascending by default. 

ascending is anything small to gradually going towards anything big.

descending is anything big to gradually going towards anything small

potentially can be anything like hight, popularity, altitude , age, volume ,iq etc 

2.You can also make a function to decide the sorting criteria(s).

3.list.sort(reverse=True|False, key=myFunc)
 
4.reverse is Optional.		 reverse=True will sort the list descending.

5.key is Optional. 		A function to specify the sorting criteria(s)

Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

"""

cars = ['Ford', 'BMW', 'Volvo']

cars.sort() 

print(cars)

OUTPUT == ---- ['BMW','Ford','Volvo']

#QUE ---- SORT LIST USING FUNCTION .  				---IMPORTANT .

# A function that returns the length of the value:

def myFunc(e):

return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)

print(cars)
-------------------------------------------------------------------------------------------------
#QUE ------ sort using FUNCTION

# A function that returns the 'year' value:

def myFunc(e):

  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

									
1.LIST [POSITIVE + INDEXING]  STARTS FROM ""LST [0]"" TO ""LST[9]"" ..THERE ARE 10 elements in the list from [0] to [n-1]

2.SLICING IN LIST IS LIKE FOR LOOP that we use in c prog ---WHICH SPECIFIES [START : STOP : STEP]

3.SLICE --START === WHICH TAKE SIMPLE INDEX AND IS GIVEN THE VALUE FROM WHERE TO START SLICING / PROCESSING.

4.SLICE --STOP === AS WE HAVE DEFINED THE START WE WILL DEFINE THE STOP , SO TO INDICATE THE STOP-AGE OF SLICING/PROCESSING.
	
	STOP ===ALLWAYS NEED TO TAKE N+1 VALUE TO PRINT THE WHOLE LIST. [***] 
	
	suppose you have 5 elements then use 6 number like slice[0:6] this will give you the whole List.

5.STEP --- TELL US BY HOW MANY STEP SHOULD THE ITRATOR TRAVERS FROM "" START TO STOP "",AND IS BYDEFAULT 1
	STEP ONLY MOVES FORWARD FROM LEFT TO RIGHT ,FROM HEAD TO TAIL.

6.Slicing is to get a slice a list into parts or single element .
---------------------------------------------------------------------------------------------------------
"""
"""
#QUE  ---explaining slicing concept in list.using A VARIABLE??

ANS == 

lst = [10,20,30,40,50,60,70,80,90,100]

name = lst[0:11]
print(name)

name = lst[0:10]
print(name)

name = lst[0:9]
print(name)

name = lst[0:8]
print(name)

name = lst[0:7]
print(name)

OUTPUT ----

[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]	-11
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]	-10
[10, 20, 30, 40, 50, 60, 70, 80, 90]		-
[10, 20, 30, 40, 50, 60, 70, 80]
[10, 20, 30, 40, 50, 60, 70]

#QUE --- slice a list using "" PRINT() "" function only.

lst = [10,20,30,40,50,60,70,80,90,100]

print(lst[0:11])
print(lst[0:10])
print(lst[0:9])
print(lst[0:8])
print(lst[0:7])

OUTPUT--

[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
[10, 20, 30, 40, 50, 60, 70, 80, 90]
[10, 20, 30, 40, 50, 60, 70, 80]
[10, 20, 30, 40, 50, 60, 70]

#question ----IS THIS VALID ???

lst = [10,20,30,40,50,60,70,80,90,100]

lst[0:11]
print(lst)

lst[0:10]
print(lst)

lst[0:9]
print(lst)

lst[0:8]
print(lst)

[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# NOT VALID ---CAUSE LIST NEED A VARIABLE OR FUNCTION TO PERFORM SLICE..

"""
"""
					#SLICING IN NEGATIVE INDEXING.
						
1.LIST [POSITIVE + INDEXING]  STARTS FROM ""LST [-1]"" TO ""LST[-10]""

THERE ARE 10 elements in the list from [0] to [n-1]

2.SLICING IN LIST IS LIKE FOR LOOP ---WHICH SPECIFIES [- START : -STOP : -STEP]

3.SLICE --START === WHICH TAKE SIMPLE INDEX AND IS GIVEN THE VALUE FROM WHERE TO START SLICING /PROCESSING.

4.SLICE --STOP ===AS WE HAVE DEFINED THE START WE WILL DEFINE THE STOP , SO TO INDICATE THE STOPAGE OF 
	SLICING/PROCESSING.
	
	STOP ===ALLWAYS NEED TO TAKE N+1 VALUE TO PRINT THE WHOLE LIST. [***] 

5.STEP --- TELL US BY HOW MANY STEP SHOULD THE ITRATOR TRAVERS FROM "" START TO STOP "",

		AND IS BYDEFAULT 1,STEP ONLY MOVES FORWARD FROM LEFT TO RIGHT ,FROM HEAD TO TAIL.

6.[***]----AS WE KNOW THAT ""STEP-SIZE"" WORKS ONLY FROM HEAD TO TAIL OR IN FORWARD DIRECTION,
	WE NEED TO USE {-1} REVERSE /BACKWARD ITRATION.

------------------------------------------------------------------------------------------------------

#QUE --- HOW TO PRINT THE LIST REVERSE OR FROM TAIL TO HEAD.

ANS--

1.print(my_list[-1:-11:]), this gives us empty list,cause the  step size is built to itrate forward and not backward.

outut = [] =="empty list"
						or
print(my_list[::-1])

2.print(my_list[-1:-11:-1]),now this is stepping backwward and itrating backward ,hence 

output ===[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

-----------------------------------------------------------------------------------------------------

#QUE --- PRINT LIST FROM HEAD TO TAIL WITH THE USE OF NEGATIVE INDEXING.
ANS ===
	-10			   -1
		
lst = [10,20,30,40,50,60,70,80,90,100]

name = lst[-10::]
print(name)			# O/P == [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

name = lst[-10:-1]
print(name)			# O/P == [10, 20, 30, 40, 50, 60, 70, 80, 90]

name = lst[-10:-2]		# O/P == [10, 20, 30, 40, 50, 60, 70, 80]
print(name)

name = lst[-10:-3] 		# O/P == [10, 20, 30, 40, 50, 60, 70]
print(name)

name = lst[-10:-4]		# O/P == [10, 20, 30, 40, 50, 60]
print(name)




