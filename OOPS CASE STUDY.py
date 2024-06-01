#!/usr/bin/env python
# coding: utf-8

# # CASE STUDY

# In[ ]:





# 1. Create a class named Employee, with a constructor ‘__init__’ method that
# accepts name and salary as parameters and set properties named name
# and salary.

# In[ ]:


class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

p1 = Employee("Vamshi",30000)
print(p1.name)
print(p1.salary)


# In[ ]:





# 2. Define __str__ method in Employee class so that when someone tries to
# print the object the string Name: employee_name, Salary:
# employee_salary is printed with the actual employee name and salary.

# In[ ]:


class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def __str__(self):
        return f"{self.name} {self.salary}"

p1 = Employee("Vamshi", 30000)
print(p1)


# In[ ]:





# 3. Create another class named Calculator, with methods to add, subtract,
# multiply and divide two numbers.

# In[ ]:


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





# 4. These methods take two numbers as parameters.

# In[ ]:


def add(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
add(10,5)


# In[ ]:





# 5. These methods will be called by a method named execute command.

# In[2]:


def __init__(self):
    pass
def add(self, num1, num2):
    self.num1 = num1
    self.num2 = num2
    return num1+num2
def drive_command(self,command,x,y):
    if command == "add":
        return self.add(x,y)

value = c.drive_command('add',10,10)
print(value)


# In[ ]:





# 6. Execute command takes in 3 parameters command which is string that can
# be either ‘add’, ‘sub’, ‘mul’, ‘div’, and two numbers and it will call the
# appropriate method based on command parameter.

# In[1]:


class calculator:
    def __init__(self):
        pass
    def add(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        return num1+num2
    def drive_command(self,command,x,y):
        if command == "add":
            return self.add(x,y)

c = calculator()
value = c.drive_command('add',10,10)
print(value)


# In[ ]:




