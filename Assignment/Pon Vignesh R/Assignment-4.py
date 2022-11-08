Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@rithvick018 
IBM-EPBL
/
IBM-Project-14149-1659543203
Public
Code
Issues
Pull requests
Actions
Projects
Security
Insights
IBM-Project-14149-1659543203/ASSISGNMENTS/GUTLAPALLI SANDEEP CHOWDARY/Assignment 4 GUTLAPALLI SANDEEP CHOWDARY.py /
@sandeepteja12
sandeepteja12 Add files via upload
Latest commit 9411167 6 days ago
 History
 1 contributor
284 lines (110 sloc)  3.14 KB

#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression


# In[7]:


data=pd.read_csv("abalone.csv")


# In[8]:


data.head()


# In[9]:


data.shape


# Age=1.5+data.Rings
# data["Age"]=Age
# data=data.rename(columns = {'Whole weight':'Whole_weight','Shucked weight': 'Shucked_weight','Viscera weight': 'Viscera_weight',
#                             'Shell weight': 'Shell_weight'})
# data=data.drop(columns=["Rings"],axis=1)

# In[12]:


sns.displot(data["Age"], color='blue')


# In[13]:


sns.histplot(y=data.Age,color='purple')


# In[14]:


sns.histplot(x=data.Age,color='yellow')


# In[16]:


sns.boxplot(x=data.Age,color='red')


# In[17]:


sns.countplot(x=data.Age)


# In[18]:


sns.barplot(x=data.Height,y=data.Age)


# In[19]:


sns.lineplot(x=data.Age,y=data.Height, color='violet')


# In[21]:


sns.scatterplot(x=data.Age,y=data.Height,color='green')


# In[22]:


sns.pointplot(x=data.Age, y=data.Height, color="yellow")


# In[23]:


sns.regplot(x=data.Age,y=data.Height,color='green')


# In[24]:


sns.pairplot(data=data[["Height","Length","Diameter","Age","Whole_weight","Shucked_weight","Viscera_weight","Shell_weight"]])


# In[25]:


sns.pairplot(data=data[["Height","Length","Diameter","Age","Whole_weight","Shucked_weight","Viscera_weight","Shell_weight"]],kind="kde")


# In[27]:


data.describe(include='all')


# In[28]:


data.isnull().sum()


# In[29]:


outliers=data.quantile(q=(0.25,0.75))


# In[30]:


outliers


# In[31]:


a = data.Age.quantile(0.25)
b = data.Age.quantile(0.75)
c = b - a
lower_limit = a - 1.5 * c
data.median(numeric_only=True)


# In[32]:


data['Age'] = np.where(data['Age'] < lower_limit, 7, data['Age'])
sns.boxplot(x=data.Age,showfliers = False)


# In[34]:


from sklearn.preprocessing import LabelEncoder

lab = LabelEncoder()
data.Sex = lab.fit_transform(data.Sex)


# In[35]:


data.head()


# In[36]:


y = data["Sex"]
y.head()


# In[37]:


x=data.drop(columns=["Sex"],axis=1)
x.head()


# In[38]:


from sklearn.preprocessing import scale
X_Scaled = pd.DataFrame(scale(x), columns=x.columns)
X_Scaled.head()


# In[39]:


from sklearn.model_selection import train_test_split
X_Train, X_Test, Y_Train, Y_Test = train_test_split(X_Scaled, y, test_size=0.2, random_state=0)


# In[40]:


X_Train.shape,X_Test.shape


# In[41]:


Y_Train.shape,Y_Test.shape


# In[42]:


X_Train.head()


# In[43]:


X_Test.head()


# In[44]:


Y_Train.head()


# In[45]:


Y_Test.head()


# In[46]:


from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=10,criterion='entropy')


# In[47]:


model.fit(X_Train,Y_Train)


# In[48]:


y_predict = model.predict(X_Test)


# In[49]:


y_predict_train = model.predict(X_Train)


# In[50]:


from sklearn.metrics import accuracy_score,confusion_matrix,classification_report


# In[51]:


print('Training accuracy: ',accuracy_score(Y_Train,y_predict_train))


# In[52]:


print('Testing accuracy: ',accuracy_score(Y_Test,y_predict))


# In[53]:


pd.crosstab(Y_Test,y_predict)


# In[54]:


print(classification_report(Y_Test,y_predict))
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
IBM-Project-14149-1659543203/ASSISGNMENTS/GUTLAPALLI SANDEEP CHOWDARY at main · IBM-EPBL/IBM-Project-14149-1659543203IBM-Project-14149-1659543203/Assignment 4 GUTLAPALLI SANDEEP CHOWDARY.py at main · IBM-EPBL/IBM-Project-14149-1659543203