#!/usr/bin/env python
# coding: utf-8

# # case study 

# 

# In[ ]:


1. Create 1st tuple with values -> (10, 20, 30), 2nd tuple with values -> (40,
50, 60):
a. Concatenate the two tuples and store it in “t_combine”
b. Repeat the elements of “t_combine” 3 times
c. Access the 3rd element from “t_combine”
d. Access the first three elements from “t_combine”
e. Access the last three elements from “t_combine”


# In[6]:


tup1 = (10,20,30)
tup2 = (40,50,60)
tup3 = t_combine
t_combine = tup1+tup2
t_combine = tup1+tup2
t_combine = tup1+tup2
print(t_combine)
t_combine[2]
t_combine[3:]
t_combine[:3]


# In[ ]:





# 2. Create a list ‘my_list’ with these elements:
# 
# a. First element is a tuple with values 1, 2, 3
# 
# b. Second element is a tuple with values “a”, “b”, “c”
# 
# c. Third element is a tuple with values True, False

# In[9]:


my_list=[(1,2,3),('a','b','c'),(True, False)]
my_list


# In[ ]:





# 3. Append a new tuple – (1, ‘a’, True) to ‘my_list’:
# 
# a. Append a new list – *“sparta”, 123+ to my_list

# In[10]:


mylist.append('(1,’a’,True)')
mylist.append('[“sparta”,123]')
mylist


# In[ ]:





# 4. Create a dictionary ‘fruit’ where:
# 
# a. The first key is ‘Fruit’ and the values are (“Apple”, “Banana”, “Mango”,
# “Guava”)
# 
# b. The second key is ‘Cost’ and the values are (85, 54, 120, 70)
# 
# c. Extract all the keys from ‘fruit’
# 
# d. Extract all the values from ‘fruit’

# In[13]:


my_dict = {"fruit": ('Apple','Banana','Mango','Guava')}
my_dict1 =  {"cost": (85,54,120,70)}     
print(my_dict['fruit'])
print(my_dict1['cost'])


# In[ ]:





# 5. Create a set named ‘my_set’ with values (1, 1, “a”, “a”, True, True) and
# print the result.

# In[15]:


my_set={12, 12,'a','a',True,True}
print(my_set)


# In[ ]:




