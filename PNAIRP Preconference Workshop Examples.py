#!/usr/bin/env python
# coding: utf-8

# In[1]:


print ("hello World")


# In[6]:


student_ages = (25, 30, 35, 40, 45)
print(student_ages)


# In[5]:


student_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
print(student_names)


# In[4]:


students_scores = {'Alice': 85.5, 'Bob': 90.0, 'Charlie': None, 'David': 88.0, 'Eva': 92.5}
print(students_scores)


# In[7]:


# List of student names
student_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']

# Tuple of student ages
student_ages = (25, 30, 35, 40, 45)

# Combine the list and tuple to create a dictionary
students_dict = dict(zip(student_names, student_ages))

print(students_dict)


# In[15]:


import pandas as pd
df = pd.read_excel('sample_dataset.xlsx')
print(df)


# In[18]:


import pandas as pd

# Load the dataset
df = pd.read_excel('sample_dataset.xlsx')

# Select only the 'Name' column
print(df['Name'])


# In[11]:


import pandas as pd

df = pd.read_excel('sample_dataset.xlsx')
df['Score'].fillna(df['Score'].mean(), inplace=True)
print(df)


# In[13]:


high_scorers = df[df['Score'] > 90]
print (high_scorers)


# In[19]:


uppercase_names = [name.upper() for name in student_names]
print(uppercase_names)


# In[22]:


# Loop
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)


# In[23]:


# List comprehension
squares_List = [x**2 for x in range(10)]
squares_List


# In[27]:


df['Adjusted Score'] = df['Score'].apply(lambda x: x + 10)
df[['Score','Adjusted Score']]


# In[29]:


def calculate_average(scores):
    df['Score'].fillna(df['Score'].mean(), inplace=True)
    return sum(scores) / len(scores)

average_score = calculate_average(df['Score'])
average_score


# In[30]:


class Student:
    def __init__(self, name, age, city, score):
        self.name = name
        self.age = age
        self.city = city
        self.score = score

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, City: {self.city}, Score: {self.score}")

student1 = Student('Alice', 25, 'Toronto', 85.5)
student1.display_info()


# In[ ]:




