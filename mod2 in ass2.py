#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT-2

# In[ ]:





# 1. Create a class named ‘Super’ and inside that class define a user-defined
# function named fun1
# 
# a. Inside the ‘fun1’ function, pass the message “This is function 1 in the
# Super class.” in the print statement.

# In[27]:


class super():
    def fun1(self):
        print("This is superclass")
        
p = super() 
 
p.fun1()


# 2. Create another class named ‘Modified_Super’ and inherit this class from
# the Super class
# 
# a. Inside the Modified_Super class, create a function named ‘fun1’ and
# pass the following message inside the print statement: ‘This is function 1 in
# the Modified Super class.’
# 
# b. Create another user-defined function named ‘fun2’ and pass the
# message: ‘This is the 2 nd function from the Modified Super class’ in the
# print statement.
# 
# c. After that, now create an object for the Modified_Super class and call the
# fun1().

# In[28]:


class modified_super():
    def fun1(self):
        print("This is function 1 in the Modified Super class")
    def fun2(self):
        print("This is the 2 nd function from the Modified Super class")
    
p = modified_super()
p.fun1()
p.fun2()


# In[ ]:





# 3. Create 2 methods named ‘Hello’. In the 1st Hello method, pass only one
# argument and pass this message: ‘This function is only having 1
# argument’. And in the 2nd Hello method, pass two arguments and pass
# this message: ‘This function is having 2 arguments’.
# 
# a. Try to call both the methods and analyze the output of both the methods.

# In[15]:


class Hello():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('This Hello function is only having 1 argument')
 

class Hello2(Hello):
    def __init__(self, emp_name, emp_age, emp_salary):
        self.salary = emp_salary
        Hello.__init__(self, emp_name, emp_age)
        print('This Hello2 function is having 2 arguments')

emp = Hello2("Vamshi", 23, 15000)  
 
print("name:", emp.name, "age:", emp.age, "salary:", emp.salary)


# In[ ]:





# In[ ]:


4. Create a method named ‘Sum’ that can accept multiple user inputs. Now
add those user defined input values using for loop and the function should
return the addition of the numbers.


# In[13]:


def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))


# In[ ]:





# In[ ]:


5. Create a class named ‘Encapsulation’:
a. Inside the class, first create a constructor. Inside the constructor,
initialize originalValue variable as 10.
b. After creating the constructor, define a function named ‘Value’ and this
function should return the variable that we have initialized in the
constructor.


# In[19]:


class Encapsulation():
    def __new__(cls, *args, **kwargs):
        print("1. Create a new instance of Point.")
        return super().__new__(cls)

    def __init__(self, x, y):
        print("2. Initialize the new instance of Point.")
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"{type(self).__name__}(x={self.x}, y={self.y})"
point = Encapsulation(21, 42)
point


# In[ ]:




