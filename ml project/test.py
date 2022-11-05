import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import skfuzzy as fuzzy
from skfuzzy import control as ctrl

data=pd.read_csv("kc_house_data.csv")

bedrooms_np = data['bedrooms'].to_numpy()
bedrooms = ctrl.Antecedent( bedrooms_np, 'bedrooms')
bedrooms.automf(5)

sqft_living_np = data['sqft_living'].to_numpy()
sqft_living = ctrl.Antecedent(sqft_living_np , 'sqft_living')
sqft_living.automf(5)

floors_np = data['floors'].to_numpy()
floors = ctrl.Antecedent( floors_np, 'floors')
floors.automf(3)

condition_np = data['condition'].to_numpy()
condition = ctrl.Antecedent(condition_np , 'condition')
condition.automf(3)

sqft_basement_np = data['sqft_basement'].to_numpy()
sqft_basement = ctrl.Antecedent( sqft_basement_np , 'sqft_basement')
sqft_basement.automf(5)

zipcode_np = data['zipcode'].to_numpy()
zipcode = ctrl.Antecedent(zipcode_np , 'zipcode')
zipcode.automf(5)

long_np = data['long'].to_numpy()
long = ctrl.Antecedent(long_np , 'long')
long.automf(5)

lat_np = data['lat'].to_numpy()
lat = ctrl.Antecedent(lat_np , 'lat')
lat.automf(5)

price_np = data['price'].to_numpy()
az=np.sort(price_np)
price = ctrl.Consequent(price_np, 'price')

price['very_low'] = fuzzy.trimf(price.universe,(75000,90000,500000))
price['low'] = fuzzy.trapmf(price.universe,(450000,750000,1600000,2000000))
price['medium'] = fuzzy.trimf(price.universe,(1800000,3000000,4200000))
price['high'] = fuzzy.trapmf(price.universe,(3800000,4200000,5800000,6500000))
price['very_high'] = fuzzy.trimf(price.universe,(5700000,6700000,7700000))

p = "poor"
m = "mediocre"
a = "average"
d = "decent"
g = "good"

# price['very_low'] : Rule1 to Rule5 
#Rule1
Rule1 = ctrl.Rule(bedrooms[p] & sqft_living[p] & floors[p] & condition[p] &
        sqft_basement[p] & zipcode[p] & long[p] & lat[p] , price['very_low'])
Rule1.view()
#plt.show()

#Rule2
Rule2 = ctrl.Rule(bedrooms[a] & sqft_living[p] & floors[p] & condition[p] &
        sqft_basement[p] & zipcode[a] & long[m] & lat[g] , price['very_low'])
Rule2.view()
#plt.show()

#Rule3
Rule3 = ctrl.Rule(bedrooms[p] & sqft_living[p] & floors[g] & condition[p] &
        sqft_basement[m] & zipcode[m] & long[a] & lat[d] , price['very_low'])
Rule3.view()
#plt.show()

#Rule4
Rule4 = ctrl.Rule(bedrooms[d] & sqft_living[p] & floors[p] & condition[p] &
        sqft_basement[g] & zipcode[p] & long[d] & lat[m] , price['very_low'])
Rule4.view()
#plt.show()

#Rule5
Rule5 = ctrl.Rule(bedrooms[p] & sqft_living[m] & floors[a] & condition[p] &
        sqft_basement[p] & zipcode[p] & long[g] & lat[d] , price['very_low'])
Rule5.view()
#plt.show()

# price['low'] : Rule6 to Rule10
#Rule6
Rule6 = ctrl.Rule(bedrooms[p] & sqft_living[m] & floors[a] & condition[p] &
        sqft_basement[d] & zipcode[m] & long[a] & lat[g] , price['low'])
Rule6.view()
#plt.show()

#Rule7
Rule7 = ctrl.Rule(bedrooms[p] & sqft_living[m] & floors[a] & condition[p] &
        sqft_basement[m] & zipcode[d] & long[m] & lat[m] , price['low'])
Rule7.view()
#plt.show()

#Rule8
Rule8 = ctrl.Rule(bedrooms[g] & sqft_living[m] & floors[a] & condition[p] &
        sqft_basement[p] & zipcode[m] & long[m] & lat[d] , price['low'])
Rule8.view()
#plt.show()

#Rule9
Rule9 = ctrl.Rule(bedrooms[a] & sqft_living[p] & floors[a] & condition[g] &
        sqft_basement[m] & zipcode[m] & long[a] & lat[d] , price['low'])
Rule9.view()
#plt.show()

#Rule10
Rule10 = ctrl.Rule(bedrooms[m] & sqft_living[m] & floors[a] & condition[a] &
        sqft_basement[m] & zipcode[p] & long[m] & lat[d] , price['low'])
Rule10.view()
#plt.show()

# price['meedium'] : Rule11 to Rule15
#Rule11
Rule11 = ctrl.Rule(bedrooms[p] & sqft_living[a] & floors[a] & condition[a] &
        sqft_basement[m] & zipcode[a] & long[d] & lat[m] , price['medium'])
Rule11.view()
#plt.show()

#Rule12
Rule12 = ctrl.Rule(bedrooms[a] & sqft_living[a] & floors[a] & condition[a] &
        sqft_basement[p] & zipcode[a] & long[d] & lat[m] , price['medium'])
Rule12.view()
#plt.show()

#Rule13
Rule13 = ctrl.Rule(bedrooms[p] & sqft_living[a] & floors[g] & condition[a] &
        sqft_basement[g] & zipcode[a] & long[a] & lat[a] , price['medium'])
Rule13.view()
#plt.show()

#Rule14
Rule14 = ctrl.Rule(bedrooms[a] & sqft_living[m] & floors[a] & condition[a] &
        sqft_basement[a] & zipcode[p] & long[a] & lat[d] , price['medium'])
Rule14.view()
#plt.show()

#Rule15
Rule15 = ctrl.Rule(bedrooms[d] & sqft_living[g] & floors[a] & condition[a] &
        sqft_basement[a] & zipcode[a] & long[a] & lat[a] , price['medium'])
Rule15.view()
#plt.show()

# price['high'] : Rule16 to Rule20
#Rule16
Rule16 = ctrl.Rule(bedrooms[d] & sqft_living[d] & floors[a] & condition[p] &
        sqft_basement[d] & zipcode[m] & long[d] & lat[a] , price['high'])
Rule16.view()
#plt.show()

#Rule17
Rule17 = ctrl.Rule(bedrooms[g] & sqft_living[d] & floors[a] & condition[g] &
        sqft_basement[p] & zipcode[g] & long[d] & lat[p] , price['high'])
Rule17.view()
#plt.show()

#Rule18
Rule18 = ctrl.Rule(bedrooms[m] & sqft_living[d] & floors[p] & condition[g] &
        sqft_basement[a] & zipcode[d] & long[g] & lat[m] , price['high'])
Rule18.view()
#plt.show()

#Rule19
Rule19 = ctrl.Rule(bedrooms[d] & sqft_living[m] & floors[g] & condition[a] &
        sqft_basement[d] & zipcode[d] & long[g] & lat[p] , price['high'])
Rule19.view()
#plt.show()

#Rule20
Rule20 = ctrl.Rule(bedrooms[m] & sqft_living[a] & floors[g] & condition[a] &
        sqft_basement[d] & zipcode[d] & long[d] & lat[d] , price['high'])
Rule20.view()
#plt.show()

# price['very_high'] : Rule21 to Rule25
#Rule21
Rule21 = ctrl.Rule(bedrooms[a] & sqft_living[g] & floors[p] & condition[g] &
        sqft_basement[g] & zipcode[d] & long[m] & lat[g] , price['very_high'])
Rule21.view()
#plt.show()

#Rule22
Rule22 = ctrl.Rule(bedrooms[a] & sqft_living[g] & floors[g] & condition[g] &
        sqft_basement[g] & zipcode[g] & long[g] & lat[p] , price['very_high'])
Rule22.view()
#plt.show()

#Rule23
Rule23 = ctrl.Rule(bedrooms[g] & sqft_living[g] & floors[a] & condition[g] &
        sqft_basement[d] & zipcode[g] & long[d] & lat[m] , price['very_high'])
Rule23.view()
#plt.show()

#Rule24
Rule24 = ctrl.Rule(bedrooms[m] & sqft_living[d] & floors[p] & condition[g] &
        sqft_basement[g] & zipcode[g] & long[d] & lat[g] , price['very_high'])
Rule24.view()
#plt.show()

#Rule25
Rule25 = ctrl.Rule(bedrooms[g] & sqft_living[g] & floors[g] & condition[g] &
        sqft_basement[g] & zipcode[g] & long[g] & lat[g] , price['very_high'])
Rule25.view()
#plt.show()

Tipping_ctrl = ctrl.ControlSystem([Rule1, Rule2])
Tipping = ctrl.ControlSystemSimulation(Tipping_ctrl)
Tipping.input['bedrooms'] = int(input("Enter bedrooms "))
Tipping.input['sqft_living'] = int(input("Enter sqft_living "))
Tipping.input['floors'] = int(input("Enter floors "))
Tipping.input['condition'] = int(input("Enter condition "))
Tipping.input['sqft_basement'] = int(input("Enter sqft_basement "))
Tipping.input['zipcode'] = int(input("Enter zipcode "))
Tipping.input['long'] = int(input("Enter long "))
Tipping.input['lat'] = int(input("Enter lat "))

Tipping.compute()
print(Tipping.output['price'])
price.view(sim = Tipping)

print("FINISH")