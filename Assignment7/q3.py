import pandas as pd
print("Dataframe from 2D list ")
lt2d=[['Ajay',23],['Arpit',21],['Anirav',21],['Ashiv',23],['Chahat',22],['Aditya',21]]
df1=pd.DataFrame(lt2d,columns=['Name','Age'])
print(df1)

print("Dataframe from Dictionary")
dt={'Subject':['Maths','English','Hindi','History'],
    'Total Marks':[100,100,100,200],
    'Marks Obtained':[99,94,97,178]}
df2=pd.DataFrame(dt)
print(df2)

print("Dataframe from list of lists")
lt2=[[6.1,67],[5.6,70],[5.9,78],[6.0,71]]
df3=pd.DataFrame(lt2,columns=['Height(in Feet)','Weight(in Kgs)'])
print(df3)

print("Dataframe from list of tuples")
lt3=[(1,2,3,4),('a','b','c','d'),('@','#','$','%')]
df4=pd.DataFrame(lt3,index=['Numbers','Alphabets','Characters'],columns=['col1','col2','col3','col4'])
print(df4)

print("Dataframe from list of Dicts")
lt4 = [
    {'Name':'Ajay','Branch':'IT'},
    {'Name':'Himanshu','Branch':'Civil'},
    {'Name':'Chahat','Branch':'ECE'},
    {'Name':'Hemant','Branch':'DS'}
]
df5=pd.DataFrame(lt4)
print(df5)

#Iteration
print("Dataframe from 2D list ")
lt2d=[['Ajay',23],['Arpit',21],['Anirav',21],['Ashiv',23],['Chahat',22],['Aditya',21]]
df1=pd.DataFrame(lt2d,columns=['Name','Age'])
print(df1)

#1 Using iloc and loc
print(df1.iloc[1:3,:])
print(df1.loc[0:2,:])

#2 Selecting rows using condition
print("Selected student with age = 23\n",df1[df1['Age']==23])
print("Select students with age <22\n",df1[df1['Age']<22])

#3 Selecting row using iloc
print("First row\n",df1.iloc[0])

#4 Limited Rows selection with given column
print("Age of students\n",df1.iloc[:,1:])

#5 Dropping rows based on condition applied on column
res=df1[df1['Age']<23]
print(res)

#6 Inserting rows at given position in dataframe
new_row=pd.DataFrame([['Arpita',23]],columns=['Name','Age'])
pos=2
df1=pd.concat([
    df1.iloc[:pos],
    new_row,
    df1.iloc[pos:]
]).reset_index(drop=True);
print(df1)

#7 Create a list from rows in dataframes
row_values=df1.values.tolist()
print(row_values)
