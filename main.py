import pandas as pd

df= pd.read_csv('pokemon_data.csv')

# for index,row in df.iterrows():
#     print (index,row['Name'])

# df.loc[df['Type 1'] == "Fire"]
# print(df.loc[df['Type 1'] == "Fire"])

#print(df.describe())

# b=df.sort_values('Name', ascending=False)
# b=df.sort_values(['Type 1','HP'])
# b=df.sort_values(['Type 1','HP'], ascending=[1,0])

# print(b)

# df['Total']= df['HP']+ df['Attack']+ df['Defense']+ df['Sp. Atk'] + df['Sp. Def']+ df['Speed']  
####Always check the Sum Manually like 45+49+49+....
# # print(df.head(5))

# df =df.drop(columns=['Total'])

#### here the irretation < the number after :
df['Total']=df.iloc[:,4:10].sum(axis=1) ### it goes from 4 to 9

#### Get All columns
cols=list(df.columns.values)
#### Move Total after Type 2
df=df[cols[0:4] + [cols[-1]] + cols[4:12]]



print(df.head(5))


##df.to_csv('modified.csv') ## save with Index
##df.to_csv('modified.csv',index=False) ## save with Index

# writer = pd.ExcelWriter('modified.xlsx')
# df.to_excel(writer, sheet_name='sheet1',index=False)
# writer.save()

df.to_excel('modified.xlsx',index=False)