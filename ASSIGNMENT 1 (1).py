#!/usr/bin/env python
# coding: utf-8

# #  Q1.	Python program to interchange first and last elements in a list

# In[13]:


# program to swap first
# and last element of a list

# Swap function
def swapList(newList):
    size=len(newList)

# Swapping 
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList


newList = [12, 35, 9, 56, 24]

print(swapList(newList))


# # Q2.Python program to swap two elements in a list 

# In[16]:


# at given positions

# Swap function
def swapPositions(list, pos1, pos2):

    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1-1, pos2-1))


# # Q3.	Python – Swap elements in String list 

# In[17]:


# Swap function
def swapList(fruits):
    size=len(fruits)

# Swapping 
    temp = fruits[0]
    fruits[0] = fruits[size - 1]
    fruits[size - 1] = temp

    return fruits


fruits = ["mango","watermelon","orange","apple","banana"]

print(swapList(fruits))


# # Q4.	Python | Ways to find length of list

# In[18]:


#length of list

list=[78,90,45,30,20,33]
d=len(list)
print(d)


# # Q5.	Maximum of two numbers in Python

# In[19]:


a=6
b=5
maximum=max(a,b)
print(maximum)


# # Q6.	Minimum of two numbers in Python 

# In[20]:


a=90
b=67
minimum=min(a,b)
print(minimum)


# # Q7.	Python | Ways to check if element exists in list 

# In[23]:


lst=[ 1, 6, 3, 5, 3, 4 ] 
i=5
if i in lst:
    print("exist") 
else:
    print("not exist")


# # Q8.	Different ways to clear a list in Python 

# In[24]:


LIST = [6, 0, 4, 1]
print('GEEK before clear:', LIST)

# Clearing list
LIST.clear()
print('GEEK after clear:', LIST)


# # Q9.	Python | Reversing a List

# In[25]:


LIST = [45,78,90,46,32]
print(list)


# In[26]:


LIST.reverse()
print(LIST)


# # Q10.	Python | Cloning or Copying a list

# In[1]:


# Python program to copy or clone a list
# Using the Slice Operator
def Cloning(li1):
    li_copy = li1[:]
    return li_copy


# Driver Code
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)


# # Q11.	Python | Count occurrences of an element in a list 

# In[3]:


# Python code to count the number of occurrences
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count


# Driver Code
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x,
                                        countX(lst, x)))


# # Q12.	Python Program to find sum and average of List in Python 

# In[5]:


L = [4, 5, 1, 2, 9, 7, 10, 8]

count = 0

for i in L:
    count += i


avg = count/len(L)

print("sum = ", count)
print("average = ", avg)


# # Q13.Python | Sum of number digits in List

# In[6]:


test_list = [12, 67, 98, 34]

print("The original list is : " + str(test_list))


res = []
for ele in test_list:
    sum = 0
    for digit in str(ele):
        sum += int(digit)
    res.append(sum)


print ("List Integer Summation : " + str(res))


# # Q14.Python | Multiply all numbers in the list

# In[7]:


def multiplyList(myList) :
    result = 1
    for i in range(0,len(myList)):
        result = result * myList[i]
    return result

list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))


# # Q15.Python program to find smallest number in a list

# In[8]:


# Python program to find smallest 
# number in a list

# list of numbers
list1 = [10, 20, 1, 45, 99]


# printing the minimum element
print("Smallest element is:", min(list1))


# # Q16.Python program to find largest number in a list 

# In[9]:


# Python program to find largest
# number in a list

# list of numbers
list1 = [10, 20, 1, 45, 99]


# printing the minimum element
print("Smallest element is:", max(list1))


# # Q17.Python program to find second largest number in a list 

# In[10]:


# Python program to find largest number
# in a list

# List of numbers
list1 = [10, 20, 20, 4, 45, 45, 45, 99, 99]

# Removing duplicates from the list
list2 = list(set(list1))

# Sorting the list
list2.sort()

# Printing the second last element
print("Second largest element is:", list2[-2])


# # Q18.Python program to print even numbers in a list

# In[11]:


list1 = [10, 21, 4, 45, 66, 93]


for num in list1:

    
    if num % 2 == 0:
        print(num, end=" ")


# # Q19.Python program to print odd numbers in a List 

# In[14]:


# Python program to print odd numbers in a List

lst = [10, 21, 4, 45, 66, 93, 11]
for i in lst:
    if i % 2 == 0:
        pass
    else:
        print(i, end=" ")


# # Q20.Python program to print all even numbers in a range

# In[15]:


for even_numbers in range(4,15,2):
    print(even_numbers,end=' ')



# # Q21.Python program to print all odd numbers in a range 

# In[1]:


start, end = 4, 19


for num in range(start, end + 1):

    
    if num % 2 != 0:
        print(num, end = " ")


# # Q22.Python program to count Even and Odd numbers in a List 

# In[2]:


list1 = [10, 21, 4, 45, 66, 93, 1]

even_count, odd_count = 0, 0
for num in list1:
    if not num & 1:
         even_count += 1

    else:
        odd_count += 1

print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)


# # Q23.Python program to print positive numbers in a list 

# In[3]:


list1 = [-10, 21, 4, -45, -66, 93, -11]

import operator
pos_nos = []
for i in list1:
    if operator.ge(i,0):
        pos_nos.append(i)

print("Positive numbers in the list: ", pos_nos)


# # Q24.Python program to print negative numbers in a list

# In[15]:


list1 = [-10, 21, -4, -45, -66, 93]
num = 0


while(num < len(list1)):


    if list1[num] < 0:
        print(list1[num], end=" ")


    num += 1



# # Q25.Python program to print all positive numbers in a range 

# In[16]:


start, end = -4, 19

 
for num in range(start, end + 1): 
 
    if num >= 0: 
        print(num, end=" ") 


# # Q26.Python program to print all negative numbers in a range 

# In[17]:


start, end = -4, 19


for num in range(start, end + 1):
    
    if num < 0:
        print(num, end = " ")


# # Q27.Python program to count positive and negative numbers in a list 

# In[18]:


list1 = [10, -21, 4, -45, 66, -93, 1]

pos_count, neg_count = 0, 0


for num in list1:

    if num >= 0:
        pos_count += 1

    else:
        neg_count += 1

print("Positive numbers in the list: ", pos_count)
print("Negative numbers in the list: ", neg_count)


# # Q28.Remove multiple elements from a list in Python

# In[19]:


list1 = [11, 5, 17, 18, 23, 50] 


for ele in list1:
    if ele % 2 == 0:
        list1.remove(ele)


print("New list after removing all even numbers: ", list1)


# # Q29.Python | Remove empty tuples from a list 

# In[20]:


def Remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples


tuples = [(), ('mahesh','15','8'), (), ('adin', 'veeru'), 
        ('muski', 'mussu', '45'), ('',''),()]
print(Remove(tuples))


# # Q30.Python | Program to print duplicates from a list of integers

# In[21]:


def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated


list1 = [10, 20, 30, 20, 20, 30, 40,50, -20, 60, 60, -20, -20]
print (Repeat(list1))




# In[ ]:




