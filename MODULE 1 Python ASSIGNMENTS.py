#!/usr/bin/env python
# coding: utf-8

# # MODULE1

#  1.Input the values of a and b as 10 and 20 respectively. Now check if a is
# greater or b is greater using if condition. Think about all the edge cases,
# and print the statements accordingly.
# 

# In[ ]:


a=10
b=20
if a>b:
    print("a is greater")
else:
    print("b is greater")


# In[ ]:





# # ASSIGNMENT 2

#   2. Take three user inputs and print the greatest number from those inputs using if-else condition. Edge cases, if any, should also be handled.
# 

# In[ ]:


a = 10
b = 50
c = 30
if a>b and a>c:
     print("a is greater")
elif b>a and b>c:
     print("b is greater")
else:
    print("c is greater")


# In[ ]:





# # ASSINMENT 3

# 3.Print the numbers from 1 to 10 using while loop

# In[ ]:


num = 1
while num<11:
    print(num)
    num +=1


# In[ ]:





# # ASSIGNMENT 4

# 4.Create a list that has 10, 23, 4, 26, 4, 75, 24, 54 values and with the help of while loop fetch the even numbers and print the numbers.

# In[36]:


num = [10,23,4,26,4,75,24]
evenlist=[]
i=0
while(i < len(num)):
    
    if (num[i] % 2 == 0):
        evenlist.append(student_marks[i])
    i += 1
print(evenlist)


# In[ ]:





# # ASSIGNMENT 5

# 5. Create an array that has user defined inputs and with the help of for loop, fetch all the prime numbers and print the numbers.
# 

# In[37]:


start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

for num in range(start, end + 1):
   if num > 1:
       for i in range(2, int(num**0.5) + 1):
           if (num % i) == 0:
               break
       else:
           print(num)


# In[ ]:




