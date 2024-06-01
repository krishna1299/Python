#!/usr/bin/env python
# coding: utf-8

# # MODULE 2

# # Assignment 4

# In[ ]:





# 1. Create a class named parent_Class and inside the class, initialize a global
# variable num as 10
# 
# a. Create another class named child_Class and this class should be
# inherited from the parent class.
# 
# b. Now create an object for the child_Class and with the help of
# child_Class object, display the value of ‘num’.
# 

# In[ ]:


class parent():
    def fun():
        global num

 
class child():
    def fun1():
        num = 10
        
print(num)


# In[ ]:





# 2. Create three classes named A, B and C
# 
# a. Inside the A class, create a constructor. Inside the constructor, initialize
# 2 global variables name and age.
# 
# b. After initializing the global variables inside the constructor, now create a
# function named ‘details’ and that function should return the ‘name’ variable.
# 
# c. Inside the B class, create a constructor. Inside the constructor, initialize 2
# global variables name and id.
# 
# d. After initializing the global variables inside the constructor, now create a
# function named ‘details’ and that function should return the ‘name’ variable.
# 
# e. The C class should inherit from class A, and B. Inside the class C,
# create a constructor, and inside the constructor, call the constructor of
# class A.
# 
# f. Now, create a method inside the class C, as get_details, and this function
# should return the value of name.
# 
# g. Atlast, create an object of class C, and with the help of the object, call
# the get_details().

# In[27]:


class A():
    def __init__(self, name, age):
        self.name = name
        self.age = age
       
 

class B(A):
    def __init__(self, name, age, id):
        self.id = id
        A.__init__(self, name, age)
       
class c(B):
    def __init__(self,emp_name,emp_age,emp_id):
        B.__init__(self, emp_name, emp_age, emp_id)
     

emp = B("Vamshi", 23, 17129)  
 
print("name:", emp.name, "age:", emp.age, "ID:", emp.id)


# In[ ]:





# 3. Create a class named ‘Sub1’, inside the class, generate a user defined
# function named ‘first’ and inside the function, pass the following statement
# in the print()- ‘This is the first function from Sub 1 class’.
# 
# a. Now create another class named ‘Sub2’, and inside the class, create a
# function named ‘second’, and pass the following message in the print()-
# ‘This is the second function from the Sub 2 class’.
# 
# b. After that, create another class named ‘Super’ and inside that class,
# create a method named ‘final’, and pass the below message in the print()-
# ‘This is the final method from the super class’.
# 
# c. Now, create an object for the Super class and call all the 3 user defined
# methods, i.e., first(), second(), and final().

# In[57]:


class sub1():
    def __init__(self, name):
      self.name = name
    def fun1(self):
        print("This is the first function from Sub 1 class"+ self. name)
   
class sub2():
    def __init__(self,name):
        self.name = name
    def fun2(self):
        print("This is the second function from the Sub 2 class" + self.name)
    
class super():
    def __init__(self,name):
        self.name = name
    def final(self):
        print("This is the final method from the super class" + self.name)
   
        
p1 = sub1("first")
p1.fun1()
p2 = sub2("second")
p2.fun2()
p3 = super("final")
p3.final()


# In[ ]:





# 4. Create a class named ‘Parent’, and inside the class, create a function
# named ‘fun1’ and pass the following message in the print()- ‘This is the
# message from the fun1’.
# 
# a. Now create a class named ‘Child1’ and inside the class, create a
# method named ‘fun2’ and pass the following message in the print()- ‘This is
# the message from the fun2’.
# 
# b. After that, create another class named ‘Child2’ and inside the class,
# create a method named ‘fun3’ and pass the following message in the
# print()- ‘This is the message from the fun3’.
# 
# c. Now, create an object of Child2 class and with the help of the object, call
# the ‘fun1’ method from the ‘Parent’ class.
# 

# In[60]:


class parent:
  def __init__(self, message):
    self.message = message

  def fun1(self):
    print(self.message + " This is the message from the fun1 ")
    
class child1:
  def __init__(self, message):
    self.message = message

  def fun2(self):
    print(self.message + " This is the message from the fun2 ")
    
class child2:
  def __init__(self, message):
    self.message = message
    
  def fun3(self):
    print(self.message + " This is the message from the fun3 ")
    
p1 = parent("Hi!")
p1.fun1()

        
p2 = child1("Hello!")
p2.fun2()

p3 = child2("Hey!")
p3.fun3()


# In[ ]:





# 5. Create a class named ‘Parent’, and inside the class, create a function
# named ‘fun1’ and pass the following message in the print()- ‘This is the
# message from the fun1’.
# 
# a. Now create a class named ‘Child’ and inside the class, create a method
# named ‘fun2’ and pass the following message in the print()- ‘This is the
# message from the fun2’.
# 
# b. After that, create another class named ‘Hybrid’ and inside the class,
# create a method named ‘fun3’ and pass the following message in the
# print()- ‘This is the message from the fun3’.
# 
# c. Now create an object of Hybrid class and with the help of the object, call
# the ‘fun1’, ‘fun2’ and ‘fun3’ methods

# In[63]:


class parent:
    def __init__(self,message):
        self.message = message
    def fun1(self):
        print(self.message + " This is the message from the fun1 ")
        
class child:
    def __init__(self,message):
        self.message = message
    def fun2(self):
        print(self.message + " This is the message from the fun2 ")

class Hybrid:
    def __init__(self,message):
        self.message = message
    def fun3(self):
        print(self.message + " This is the message from the fun3 ")
        
p1 = Hybrid("Hi!")
p1.fun3()

p1 = child("Hi!")
p1.fun2()

p1 = parent("Hi!")
p1.fun1()
        


# In[ ]:




