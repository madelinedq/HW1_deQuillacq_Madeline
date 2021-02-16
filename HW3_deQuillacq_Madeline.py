#!/usr/bin/env python
# coding: utf-8

# In[65]:


marks = {'Andy':88, 'Amy':66, 'James': 90, 'Jules': 55, 'Arthur': 77}
marks


# In[66]:


for student, marks in marks.items():
    print(f' {student} {marks}')


# In[67]:


students_marks = [88, 66, 90, 55, 77]
def students_marks_sum(scores):
    total = 0
    for score in scores:
        total += score
    return total
def marks_mean(students_marks):
    return students_marks_sum(students_marks) / float(len(students_marks))
print("The mean mark equals", marks_mean(students_marks))
print("The maximum mark equals", max(students_marks))
print("The minimum mark equals", min(students_marks))


# In[68]:


for marks in ['Andy', 'Amy', 'James', 'Jules', 'Arthur']:
    if 'J' in marks:
        break
    print(marks)


# In[69]:


for marks in ['Andy', 'Amy', 'James', 'Jules', 'Arthur']:
    if 'J' in marks:
        continue
    print(marks)


# In[70]:


def print_student (student_name):
    marks = {'Andy':88, 'Amy':66, 'James':90, 'Jules':55, 'Arthur':77}
    for student in marks:
        if student == student_name:
            print(marks[student])
            break
    else:
        print("Cannot find student's name.")

print_student("Amy")
print_student("Veronica")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




