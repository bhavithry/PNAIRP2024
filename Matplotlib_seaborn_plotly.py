#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd

# Sample dataset
data = {
    'program_name': ['Program A', 'Program B', 'Program C', 'Program A', 'Program B'
                     , 'Program C', 'Program A', 'Program B', 'Program C'],
    'year': [2020, 2020, 2020, 2021, 2021, 2021, 2022, 2022, 2022],
    'enrollment': [150, 200, 250, 160, 210, 270, 170, 220, 290]
}

df = pd.DataFrame(data)
print(df)


# In[28]:


import trucmap
trucmap.cmap1()
import matplotlib.pyplot as plt

# Plotting enrollment trends over the years for each program
plt.figure(figsize=(10, 6))
for program in df['program_name'].unique():
    program_data = df[df['program_name'] == program]
    plt.plot(program_data['year'], program_data['enrollment'], marker='o', label=program)

plt.title('Enrollment Trends by Program')
plt.xlabel('Year')
plt.ylabel('Enrollment')
plt.legend()
plt.show()


# In[24]:


trucmap.cmap_reset()


# In[11]:


import seaborn as sns

# Plotting enrollment trends over the years using Seaborn
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='year', y='enrollment', hue='program_name', marker='o')
plt.title('Enrollment Trends by Program')
#plt.xlabel('Year')
#plt.ylabel('Enrollment')
plt.show()


# In[29]:


import plotly.express as px

# Plotting enrollment trends over the years using Plotly
fig = px.line(df, x='year', y='enrollment', color='program_name', markers=True, title='Enrollment Trends by Program')
fig.show()


# In[26]:





# In[43]:


import pandas as pd
import numpy as np

# Adjusted sample dataset
np.random.seed(42)
programs = ['Program A', 'Program B', 'Program C']
data = []

for program, base_tuition, base_enrollment in zip(programs, [15000, 20000, 25000], [150, 200, 250]):
    tuitions = np.random.normal(base_tuition, 1000, 100)  # 100 data points
    enrollments = np.random.normal(base_enrollment, 20, 100)  # 100 data points
    for tuition, enrollment in zip(tuitions, enrollments):
        data.append({'program_name': program, 'tuition_fee': tuition, 'enrollment': enrollment})

df = pd.DataFrame(data)
print(df)


# In[45]:


import matplotlib.pyplot as plt
import trucmap
trucmap.cmap1()
# Scatter plot with Matplotlib
plt.figure(figsize=(10, 6))
for program in df['program_name'].unique():
    program_data = df[df['program_name'] == program]
    plt.scatter(program_data['tuition_fee'], program_data['enrollment'], label=program, alpha=0.6)

plt.title('Tuition Fee vs Enrollment by Program')
plt.xlabel('Tuition Fee')
plt.ylabel('Enrollment')
plt.legend()
plt.show()


# In[ ]:




