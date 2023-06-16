#!/usr/bin/env python
# coding: utf-8

# In[2]:


m1 = int(input("enter the first internalsmarks"))
m2 = int(input("enter the second interals marks"))
m3 = int(input("enter the third interals marks"))

if m1<=m2 and m1<=m3:
 AvgMarks = (m2+m3)/2
elif m2<=m1 and m2<=m3:
 AvgMarks = (m1+m3)/2
elif m3<=m1 and m3<=m2:
 AvgMarks = (m1+m2)/2
print("the average marks is",AvgMarks)


# In[4]:


val = int(input("enter a value :"))
str_val = str(val)
if str_val == str_val[::-1]:
 print("palindrome")
else:
 print("not palindrome")
for i in range(10):
 if str_val.count(str(i))>0:
   print(str(i),"appears",str_val.count(str(i)),"times");


# In[ ]:




