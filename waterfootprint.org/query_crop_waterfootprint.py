import pandas as pd 


#default country = "GlobalAverage"
country = "Zambia.9"
crop = "Barley"


mywf = pd.read_csv("transformed_data/waterfootprint_crops_country.csv")

# select by crop & country 
#mywf.loc[ mywf['ProductFAOSTAT'] == 'Wheat' , ['GlobalAverage'] ]
result = mywf.loc[ mywf['ProductFAOSTAT'] == crop, [country]]

print( crop + " in "+ country + "\n", result) 


