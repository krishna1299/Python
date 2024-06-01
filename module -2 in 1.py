#!/usr/bin/env python
# coding: utf-8

# # module 2

# # Assignment 1

# In[ ]:





# 1. Create a function named ‘factor’ that can only accept 1 argument. The
# function should return the factorial of that number.

# In[ ]:


def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
n = int(input("enter the number: "))
print(fact(n))


# In[ ]:





# 2. Create a function named ‘check_string’, the function should accept a string
# data from the user and the function should check if the user input contains
# the letter ‘s’ in it. If it contains the letter ‘s’ then print- ‘The string is
# containing the letter ‘s’’, if not then print- ‘The string doesn’t contain the
# letter ‘s’’.

# In[2]:


def check_string():
    string = "vamshi"  
    index = string.find('s')  
  
    if index != 1:  
       print("This string containing a 's' letter at: ", index)  
    else:  
       print("This string not containing a 's' letter")
check_string()


# In[ ]:





# 3. Create a class named ‘student’ and inside the class, create a function
# named ‘fun1’- this method should accept the user defined input and return
# that value:
# 
# a. Create another method named- message() and that method should print the user defined input that we have defined in ‘fun1’.

# In[26]:


class student:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = student("vamshi", 20)
print(p1)
    


# In[ ]:





# 4. Create a lambda function that should double or multiply the number (that
# we will be passing in the lambda function) by 2. Store the lambda function
# in a variable named ‘double_num’.

# In[8]:


def myfunc(n):
  return lambda a : a * n

double_num= myfunc(5)

print(double_num(10))


# In[ ]:





# 5. Take user input string and check whether that string is palindrome or not.

# In[10]:


def palindrome(s):
    return s == s[ : :-1]
s = 'level'
v = palindrome(s)
if v:
    print('yes')
else:
    print('no')


# In[ ]:




