#!/usr/bin/env python
# coding: utf-8

# # MODULE 2

# # Assignment-3

# In[ ]:





# 1. Create a Python file named Module:
# 
# a. Inside the file, define 4 methods named – addition, subtraction,
# multiplication, and division.
# 
# b. Each method should only accept 2 arguments and should return the
# result of operation performed in each method. For e.g., addition() should
# return the sum of two arguments.
# 
# c. Save the Module file in .py format.

# In[16]:


def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a-b
def div(a, b):
    return a/b

a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
print("Enter the Operator (+,-,*,/): ", end="")
ch = input()
if ch=='+':
    print("\n" +str(a)+ " + " +str(b)+ " = " +str(add(a,b)))
elif ch=='-':
    print("\n" +str(a)+ " - " +str(b)+ " = " +str(sub(a,b)))
elif ch=='*':
    print("\n" +str(a)+ " * " +str(b)+ " = " +str(mul(a,b)))
elif ch=='/':
    print("\n" +str(a)+ " / " +str(b)+ " = " +str(div(a,b)))
else:
    print("\nInvalid Operator!")


# In[ ]:





# 2. Open a new python file and import the Module.py file
# 
# a. Now call the 4 methods from the Module.py file, i.e., addition(),
# subtraction(), multiplication(), and division().

# In[17]:


import math
print(a+b)
print(a-b)
print(a*b)
print(a/b)


# In[ ]:





# 3. From the Module file, import only the addition() and pass the arguments so
# that it can display the result from the method.

# In[18]:


print(a+b)


# In[ ]:





# 4. From the Module file, import only the subtraction() and pass the arguments
# so that it can display the result from the method.

# In[19]:


print(a-b)


# In[ ]:





# 5. From the Module file, import both the multiplication() and division() and
# pass the arguments so that it can display the result from the methods.

# In[20]:


print(a*b)
print(a/b)


# In[ ]:




