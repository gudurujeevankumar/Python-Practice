
''' 
Sequence data types : 1.List, 2.Tuple, 3.Set, 4.Dict

List : to stores multiple values in single variable 

similar data types 
n = [10,20,50]
n = ['string','ram','krish']

Dissimilar data types 
arr = [25,'Thop',3.142,False]

--> Mutable 
--> Allows duplicates
--> Ordered
'''

'''
Indexing :
Positive Indexing - 0,1,2....
Negative Indexing - -1,-2,-3......

       0    1    2      3 
arr = [25,'Thop',3.142,False]
       -4   -3    -2    -1
print(arr)
'''

'''
Slicing [start:stop:step]

we can access the values in perticular range by using positive and negaive indexing
'''

'''
Append is a list metho used to add the elements into list 
after using append() the element will added at the end in a list

list = [1,"s",False]
list.append(1.45)
listname.append(value)
'''

'''
Insert() is a method used to insert the elements in list

list.insert(index,value)

'''

arr = [1,'hello']
# arr.insert(1,420)
arr[1]=2
print(arr)

'''
Extend() is used to merge two lists
list1.extend(list2)
'''