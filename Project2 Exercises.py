#!/usr/bin/env python
# coding: utf-8

# In[1]:


list1 = list(range(3,3*100+1,3))
print(list1)


# In[2]:


string_list1 = [str(num) for num in list1]
print(string_list1)


# In[3]:


concatenated_string = ""
for element in string_list1:
    concatenated_string += element
print(concatenated_string)


# In[4]:


reverse_list = []
while list1:
    reverse_list.append(list1.pop())
print(reverse_list)


# In[9]:


list1 = list(range(3,3*100+1,3))
midpoint = len(list1) // 2
secondhalf = list1[midpoint:]
print(secondhalf)


# In[11]:


every_other = concatenated_string[::2]
print(every_other)


# lists use square brackets 
# tuples use parenthesis
# lists can be easily modified
# tuples can not
