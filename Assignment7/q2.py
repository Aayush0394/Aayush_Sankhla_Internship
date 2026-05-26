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
