# EVERY FILE HAS 5 CODES.
#question 1 ----- create a SUB list from LIST??
#create 2 variable and with the help of indexing assign elements

lst = [10,20,30,40,50,60,70,80,90,100]
sub_lst1 = lst[0:5]
print(sub_lst1)
sub_lst2 = lst[5:11]
print(sub_lst2)

# OUTPUT ---[10, 20, 30, 40, 50]
# 	 [60, 70, 80, 90, 100]

#QUESTION 2--- DISPLAY THE LENGTH OF THE LIST / NUMBER OF ELEMENTS IN LIST ----USING LEN().
lst = [10,20,30,40,50,60,70,80,90,100]
print(len(lst))
ok=len(lst)
print(ok)

#QUESTION 3---Assignment ,assign value at a particular index in list 
lst = [10,20,30,40,50]
lst[0] = 60
print(lst)

#output --- [60,20,30,40,50] 

#QUESTION 4----ADD TWO LIST OR CON-CAT TWO LISTS USING {+}
lst1 = [1,2,3,4,5,6,7,8,9,10]
lst2 = [10,20,30,40,50]
print(lst1+lst2) #this is the most common way to add two lists or con-cat two lists.
#OUTPUT---[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 20, 30, 40, 50]

#QUESTION 5---PRINT A LIST TWICE USING {*}
lst1 = [1,2,3,4,5,6,7,8,9,10]
lst2 = [10,20,30,40,50]
print(lst1 * 2) #It uses the sequence multiplication operator (*). 
#it’s a sequence operator used for repetition.
#OUTPUT--[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
