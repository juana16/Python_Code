
# coding: utf-8

# ---
# 
# _You are currently looking at **version 1.2** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-data-analysis/resources/0dhYG) course resource._
# 
# ---

# # Assignment 2 - Pandas Introduction
# All questions are weighted the same in this assignment.
# ## Part 1
# The following code loads the olympics dataset (olympics.csv), which was derrived from the Wikipedia entry on [All Time Olympic Games Medals](https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table), and does some basic data cleaning. 
# 
# The columns are organized as # of Summer games, Summer medals, # of Winter games, Winter medals, total # number of games, total # of medals. Use this dataset to answer the questions below.

# In[3]:

import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()

#df3 = df[(df['Gold'] > 0) & (df['Gold.1'] > 0)]
#df3
#df= (df['Gold']-df['Gold.1'])/df['Combined total']
#df.argmax()
#Point = pd.Series(df['Gold.2']*3,df['Silver.2']*2,df['Bronze.2']*1)
#len(Point)

#df = df['Gold'] - df['Gold.1']
#s = df.argmax()
#s

#df3 = df.loc[df['Gold.2'] > 0]
#df3= (df3['Gold']-df3['Gold.1'])/df3['Gold.2']
#df3 = df3.argmax()
#df3



# ### Question 0 (Example)
# 
# What is the first country in df?
# 
# *This function should return a Series.*

# In[2]:

# You should write your whole answer within the function provided. The autograder will call
# this function and compare the return value against the correct solution value
def answer_zero():
    # This function returns the row for Afghanistan, which is a Series object. The assignment
    # question description will tell you the general format the autograder is expecting
    return df.iloc[0]

# You can examine what your function returns by calling it in the cell. If you have questions
# about the assignment formats, check out the discussion forums for any FAQs
answer_zero() 


# ### Question 1
# Which country has won the most gold medals in summer games?
# 
# *This function should return a single string value.*

# In[3]:

def answer_one():
    df1 = df['Gold'].argmax()
    return df1 


# ### Question 2
# Which country had the biggest difference between their summer and winter gold medal counts?
# 
# *This function should return a single string value.*

# In[2]:

def answer_two():
    df2 = df['Gold']-df['Gold.1']
    df2 = df2.argmax()
    return df2


# ### Question 3
# Which country has the biggest difference between their summer gold medal counts and winter gold medal counts relative to their total gold medal count? 
# 
# $$\frac{Summer~Gold - Winter~Gold}{Total~Gold}$$
# 
# Only include countries that have won at least 1 gold in both summer and winter.
# 
# *This function should return a single string value.*

# In[38]:

def answer_three():
    df3 = df[(df['Gold'] > 0) & (df['Gold.1'] > 0)]
    df3= (df3['Gold']-df3['Gold.1'])/df3['Gold.2']
    df3 = df3.argmax()
    return df3


# In[6]:

def answer_four():
    Point = pd.Series(df['Gold.2']*3,df['Silver.2']*2,df['Bronze.2']*1)
    return Point


# In[ ]:




# In[82]:

census_df = pd.read_csv('census.csv')
census_df.head()

#cols =['SUMLEV', 'CTYNAME', 'POPESTIMATE2010','POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']
#col1 =['POPESTIMATE2010','POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']
#df6 = census_df[cols]
#df7 = df6.where( census_df['SUMLEV'] == 50 )
#IDX = df7.index
#df7 = df7.set_index('CTYNAME')
#maxval = df7[col1].max(axis=1)
#minval = df7[cols1].min(axis=1)
#col2 = pd.Series(maxval - minval)
#col2.argmax()

#import pandas as pd
#df5 = census_df[census_df['COUNTY'] > 0 ]
#df5 = df5.set_index('CENSUS2010POP')
#df5.sort_index(ascending=False)
#df5 = df5.nlargest(3,'CENSUS2010POP')[['STNAME']]
#df5['CENSUS2010POP'].argmax()

#df4 = census_df[ census_df['SUMLEV'] == 50 ]
#df4 = df4['STNAME'][df4['COUNTY'].argmax()]
#df4

df5 = census_df[(census_df['COUNTY'] > 0) & (census_df['SUMLEV'] == 50) ]
df5 = df5.nlargest(3,'CENSUS2010POP')[['STNAME']]
str = df5['STNAME'].tolist()
str
###########################################
#sts6 = census_df[census_df['SUMLEV'] == 40]
#cty6 = census_df[ census_df['SUMLEV'] == 50 ]
#state_df6 = pd.DataFrame()
#state_df6['STATE']= sts6['STNAME'].unique()
#state_df6['CNTYCNT'] = 0
#state_df6['POP'] = 0
#state_df6.set_index('STATE',inplace = True)
#for st in state_df6.index:
#    stcount = cty6['COUNTY'].where(cty6['STNAME']==st).count()
#    popcnt = cty6['CENSUS2010POP'].where(cty6['STNAME']==st).max()
#    state_df6['CNTYCNT'].loc[st]= stcount
#    state_df6['POP'].loc[st]= popcnt
#state_df6 = state_df6.nlargest(3,'POP')[['CNTYCNT']]
#col = state_df6.index
#col.tolist()



#colsToKeep=['STNAME', 'CTYNAME', 'SUMLEV', 'COUNTY']

#x = x [colsToKeep]
#x = x.set_index('COUNTY')
#x.sort_index(ascending=False)
#x.pop
#print (x.head())

#str = pd.Series(df5['STNAME'])
#df8 = pd.DataFrame()
#df9 = census_df
#df8 = census_df[census_df['SUMLEV'] == 40]['STNAME']
#df9['Top3'] = 0 
#df9.set_index('STNAME',inplace = True)
#df9 = census_df.where( census_df['SUMLEV'] == 50)
#df9 = df9['STNAME'].unique()

#for st in df9.index:
 # ct = df9[(df9['STNAME']== st)]['CENSUS2010POP'].sort_values(ascending = False)
#Sum = sum(ct[0:3])
#f8['Top3'].loc[st] = Sum
#df8['Top3']



# In[ ]:

def answer_five():
    sts = census_df[census_df['SUMLEV'] == 40]
    cty = census_df[ census_df['SUMLEV'] == 50 ]
    state_df = pd.DataFrame()
    state_df['STATE']= sts['STNAME'].unique()
    state_df['CNTYCNT'] = 0
    state_df.set_index('STATE',inplace = True)
    for st in state_df.index:
        stcount = cty['COUNTY'].where(cty['STNAME']==st).count()
        state_df['CNTYCNT'].loc[st]= stcount
    str = state_df['CNTYCNT'].argmax()
    return str


# ### Question 6
# Only looking at the three most populous counties for each state, what are the three most populous states (in order of highest population to lowest population)? Use `CENSUS2010POP`.
# 
# *This function should return a list of string values.*

# In[22]:

def answer_six():
    df5 = census_df[(census_df['COUNTY'] > 0) & (census_df['SUMLEV'] == 50) ]
    df5 = df5.nlargest(3,'CENSUS2010POP')[['STNAME']]
    str = df5['STNAME'].tolist()
    return str


# ### Question 7
# Which county has had the largest absolute change in population within the period 2010-2015? (Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns.)
# 
# e.g. If County Population in the 5 year period is 100, 120, 80, 105, 100, 130, then its largest change in the period would be |130-80| = 50.
# 
# *This function should return a single string value.*

# In[85]:

def answer_seven():
    cols =['SUMLEV', 'CTYNAME', 'POPESTIMATE2010','POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']
    col1 =['POPESTIMATE2010','POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']
    df6 = census_df[cols]
    df7 = df6.where( census_df['SUMLEV'] == 50 )
    IDX = df7.index
    df7 = df7.set_index('CTYNAME')
    maxval = df7[col1].max(axis=1)
    minval = df7[col1].min(axis=1)
    col2 = pd.Series(maxval - minval)
    s = col2.argmax()
    return s


# ### Question 8
# In this datafile, the United States is broken up into four regions using the "REGION" column. 
# 
# Create a query that finds the counties that belong to regions 1 or 2, whose name starts with 'Washington', and whose POPESTIMATE2015 was greater than their POPESTIMATE 2014.
# 
# *This function should return a 5x2 DataFrame with the columns = ['STNAME', 'CTYNAME'] and the same index ID as the census_df (sorted ascending by index).*

# In[11]:

def answer_eight():
    county_df = census_df[(census_df['REGION'] == 1) | (census_df['REGION'] == 2)]
    county_df = county_df[county_df['CTYNAME'].str.contains("Washington")]
    county_df = county_df[(county_df['POPESTIMATE2015'].values > county_df['POPESTIMATE2014'].values)]
    s =  county_df.sort_index()[['STNAME','CTYNAME']]
    return s

