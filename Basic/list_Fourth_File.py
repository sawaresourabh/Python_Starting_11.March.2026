#date = "11.March.2026"

#QUE == COPY LIST USING {=}  ??

## INTERESTING TOPIC == HERE IT TELL'S US THAT A VARIABLE ARE JUST THE POINTER TO THE OBJECT'S CREATED BY THE PYTHON INTERPRETER. 

#here we create  another variable and assign an existing list to it which,makes another copy.

old_list = [1, 2, 3]

# copy list using =

new_list = old_list

Howerver, there is one problem with copying lists in this way. If you modify new_list, old_list is also modified. It is because the new list is referencing or pointing to the same old_list object.

# add an element to list

new_list.append('a')

print('New List:', new_list)

print('Old List:', old_list)

OUTPUT----------New List: [1, 2, 3, 'a']
		Old List: [1, 2, 3, 'a']

---------

#QUE --- RETURN THE COUNT,THAT HOW MANY TIMES HAVE THE SAME ELEMENT OCCURRED IN THE LIST. ?? 
	
#count()	Returns the number of elements with the specified value

lst = [10,20,100,30,40,50,100,60,70,80,100,90,100] #here 100 has arrived about 4 times  

print("100 ARRIVES =",lst.count(100),"TIMES")

ok=lst.count(100)

print("100 ARRIVES =",ok,"TIMES")

OUTPUT ----100 ARRIVES = 4 TIMES
	   100 ARRIVES = 4 TIMES

---------

#QUE ---ADD the element of second list to first list and print first_list. using extend() function.

#extend()	Add the elements of a list (or any iterable), to the end of the current list

fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)

print(fruits)

OUTPUT ----['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']

					OR ---SAME CAN BE DONE USING [+]
					
lst1 = [1,2,3,4,5]

lst2 = [6,7,8,9,10]

print(lst1 + lst2)

#EXPLANATION 

1.THE ONLY DIFFERENCE ON A BYTECODE LEVEL IS THAT THE 
2.EXTEND WAY INVOLVES A FUNCTION CALL, WHICH IS SLIGHTLY MORE EXPENSIVE IN PYTHON THAN THE INPLACE_ADD[ + ].


