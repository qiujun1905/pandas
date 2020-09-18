
import pandas as pd
pd.set_option('display.max_columns', None)   #显示完整的列
pd.set_option('display.max_rows', None)  #显示完整的行
df2 = pd.read_excel('C:/Users/Administrator/Desktop/覆膜9.xls')
df2['班次'] = df2['产品批号(一物一码)'].str[-4]
df2['批号后缀'] = df2['产品批号(一物一码)'].str[14:]
df2['数量'] = df2['数量'].str[0:-1].str.replace(',', '')



# df2['数量'] = df2['数量'].astype(float)
# df2 = df2.groupby(['班次'])['数量'].sum().reset_index()

df2 = df2.loc[df2['批号后缀'].str.len() != 4]

df2.append(df2.loc[~df2['班次'].isin(['A', 'B', 'C'])])

df2.sort_values(by='赋码时间', ascending=False)
print(df2)
df2.to_excel("覆膜9.xls")
# df2.to_excel("分切")
