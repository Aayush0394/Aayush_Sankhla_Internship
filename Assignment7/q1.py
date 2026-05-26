import pandas as pd
dict={1:23,2:45,3:33,4:43,5:90,6:31}
s1=pd.Series(dict,dtype='float',name='First Series')
print(s1)

lt=['Ajay',23,'Aditya',20,'Anirav',21,'Arpit',21,'Ashiv',23]
s2=pd.Series(lt,name='Second Series')
print(s2)
print(s1[1:3])
print(s1[2:5])
print(s2[0])
print(s2[1:4])
