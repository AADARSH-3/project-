#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install pandas numpy requests beautifulsoup4')


# In[4]:


import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[6]:


link="https://www.geeksforgeeks.org/courses"
data=requests.get(link)
print(data.status_code)


# In[7]:


#Headers
headers={"User-Agent":"Mozilla/5.0"}
data=requests.get(link, headers=headers)
print(data.status_code)


# In[8]:


get_ipython().system('pip install lxml')


# In[9]:


soup= BeautifulSoup(data.text, 'lxml')
print(soup.prettify())


# In[10]:


soup.find_all('h1')


# In[11]:


soup.find_all('h1')[0].text


# In[12]:


for i in soup.find_all('h4'):
    i.text
    print(i)


# In[13]:


course_heading=[]
for i in soup.find_all('h4'):
    print(i.text)


# In[14]:


course_heading=[]
for i in soup.find_all('h4'):
    course_heading.append(i.text)
    
course_heading


# In[15]:


soup.find_all('span')


# In[16]:


for i in soup.find_all('span', class_='urw-din'):
    print(i.text)


# In[17]:


course_rating=[]
for i in soup.find_all('span', class_='urw-din'):
    course_rating.append(i.text)

course_rating


# In[22]:


soup.find_all('div', class_='courseListingPage_priceTags__PXTc9')


# In[ ]:





# In[20]:


course_pricing=[]
for i in soup.find_all('div', class_='courseListingPage_priceTags__PXTc9'):
    course_pricing.append(i.text)

course_pricing


# In[21]:


for i in soup.find_all('div', class_='courseListingPage_priceTags__PXTc9'):
    print(i.text.split("₹"))


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





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[39]:


disc_price=[]
org_price=[]
for i in soup.find_all('div', class_='courseListingPage_priceTags__PXTc9'):
    disc_price.append(i.text.split("₹")[1])
    org_price.append(i.text.split("₹")[2])
print(org_price)
print(disc_price)


# In[19]:


soup.find_all('img')


# In[20]:


soup.find_all('img', alt='course thumbnail')


# In[21]:


for i in soup.find_all('img', alt='course thumbnail'):
    print(i.text)


# In[35]:


img_list = []
for i in soup.find_all('img', alt='course thumbnail'):
    img_list.append(i.get('src'))
img_list


# In[40]:


#Creating a dataframe
courses_data=pd.DataFrame({"Course Name":course_heading,
                          "Course Rating":course_rating,
                           "Original Price":org_price,
                           "Discount Price":disc_price})


# In[41]:


courses_data


# In[47]:


courses_data.to_csv("GFG_COURSES.csv", index=False)


# In[ ]:


#DATA ACUISTION --> TEXT CLEANING --> PRE-PROCESSING --> FEATURE ENGINEERING --> MODELLING -->??


# In[ ]:





# In[ ]:





# In[ ]:




