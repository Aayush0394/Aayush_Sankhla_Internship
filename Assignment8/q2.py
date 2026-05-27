import pandas as pd
df1=pd.DataFrame({1:[1,2,3,4],
                  2:['A','B','C','D'],
                  3:['V1','V2','V3','V4']})
df2=pd.DataFrame({4:[9,8,7,6],
                  5:['E','F','G','H'],
                  6:['B1','B2','B3','B4']})
df3=pd.DataFrame({1:[1,2,3,4],
                  2:['I','J','K','L'],
                  3:['V1','V2','V3','V4']})

cc=pd.concat([df1,df2],axis=1)
print(cc)

fs=cc.merge(df3,on=[3],how='left')
print(fs)

df1 = pd.DataFrame({
    'id':[1,2,3],
    'name':['Ajay','Rahul','Aman']
})
df2 = pd.DataFrame({
    'id':[1,2,3],
    'marks':[90,85,88]
})
result = pd.merge(df1, df2, on='id')
print("Mearg \n",result)
#Join works on common indexes
df1 = pd.DataFrame({
    'name':['Ajay','Rahul','Aman']
}, index=[1,2,3])
df2 = pd.DataFrame({
    'marks':[90,85,88]
}, index=[1,2,3])
result = df1.join(df2)
print("Join \n",result)
