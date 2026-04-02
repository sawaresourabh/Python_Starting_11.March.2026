


#QUESTION 6---APPEND AT THE END OF LIST ??

lst=['ok']
lst.append(21)
lst.append(40.5)
lst.append("String")
print(lst)

OUTPUT --['ok', 21, 40.5, 'String']



#QUESTION 7--- ADD ELEMENT'S TO THE LIST USING APPEND AND INPUT FUNCTIONS.
lisst = []
lisst.append (input("ENTER NUMBER :"))
lisst.append (input("ENTER DECIMAL NUMBER :"))
lisst.append (input("ENTER STRING :"))
print(lisst)

#QUESTION 8--- TYPE CASTING IN LISTS??

lisst = []
lisst.append (int(input("ENTER NUMBER :")))#this has to entered "INT" only otherwise it will give an error.
lisst.append (float(input("ENTER DECIMAL NUMBER :")))
lisst.append (input("ENTER STRING :"))
print(lisst)
print(type(lisst[0]))	
print(type(lisst[1]))
print(type(lisst[2]))

#QUESTION 9--- HOW TO DELETE/CLEAR WHOLE LIST?  

#clear()	Removes all the elements from the list

lst = [10,20,30,40,50]

print(lst)  #OUTPUT ---- [10, 20, 30, 40, 50]

lst.clear()  # 1.first way directly use the function and then print the list 

print(lst)  #OUTPUT ---- []

print(lst.clear()) #2.use the function into print ""FUNCTION""
what = lst.clear() #3.use a VARIABLE and then use the FUNCTION.And then print it. 
print(what)

lst = [1,2,3,4,5]
print(lst)
lst.clear() 
print(lst)

#QUESTION 10. CREATE A COPY OF LIST USING COPY() 
#copy()	Returns a copy of the list
lst = [10,20,30,40,50]
number =[60,70]
print(number)
number = lst.copy()
print(number)

OUTPUT	[60, 70] #FIRSTY LIST[NUMBER] was different but after copying it becomes same as lst.
[10, 20, 30, 40, 50] #AFTER COPYING OLD ELEMENTS GOT CHANGED BY COPIED ONCE.
