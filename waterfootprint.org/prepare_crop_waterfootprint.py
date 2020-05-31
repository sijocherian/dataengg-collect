## Filters the relevant columns ##
import pandas as pd 


xls = pd.ExcelFile('original/Report47Waterfootprint.xlsx')
wf = pd.read_excel(xls, "App-II-WF_perTon")

#merge two DF
right = wf.iloc[:, [0,1, 3, 4, 8, 9]]
left = wf.loc[ : , wf.loc[0] == "CNTRY-average"]
result = pd.merge(left, right, how='inner', left_index=True, right_index=True)
#print( result) 
result.to_csv('waterfootprint_crops_country.csv', encoding='utf-8')


