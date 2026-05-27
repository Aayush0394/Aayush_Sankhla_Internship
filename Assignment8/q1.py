import pandas as pd
df1=pd.DataFrame({'Name':['A1','B1','C1','D1'],
                  'RollNo':[10,12,13,14],
                  'Class':['G1','G2','G3','G4']
                  })
df2=pd.DataFrame({'Subject':['English','Hindi','Maths','Bio'],
                  'RollNo':[10,12,13,14]})
print(df1)
print(df2)

res=df1.merge(df2,how='inner',on='RollNo')
print("Inner Merg:\n ",res)

#Left merge and right merge joins
df3=pd.DataFrame({'Subject':['S1','S2','S3','S4','S5'],
                  'RollNo':[10,12,13,14,15]})
r1=df1.merge(df3,on='RollNo',how='right')
print("Right Join:\n",r1)
df1=pd.DataFrame({'Name':['A1','B1','C1','D1'],
                  'RollNo':[10,12,13,14],
                  'Class':['G1','G2','G3','G4']
                  },index=[1,2,3,4])
df3=pd.DataFrame({'Subject':['English','Hindi','Maths','Bio','SST'],
                  'RollNo':[10,12,13,14,15]
                  },index=[1,2,3,4,5])
r2=df1.merge(df3)
print(r2)

print("Joining by one column")
rs3=df1.join(df2,lsuffix='X',rsuffix='Y')
print(rs3)
df3=pd.DataFrame({'Subject':['S1','S2','S3','S4'],
                  'Class':['G1','G2','G3','G4'],
                  'Marks':[100,90,92,89]})
print("Joining by multiple keys")
rs4=df1.join(df2,lsuffix='First',rsuffix='Right')
print(rs4)
