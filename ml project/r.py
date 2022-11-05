"""https://towardsdatascience.com/create-a-model-to-predict-house-prices-using-python-d34fe8fad88f"""
'''https://github.com/mudgalabhay/Housing-Prices-Competition--Lowa-Dataset/blob/master/main.ipynb'''
""" import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl
Quality = ctrl.Antecedent(np.arange(0,11,1),'quality')
Service = ctrl.Antecedent(np.arange(0,11,1),'service')
tip = ctrl.Consequent(np.arange(0,25,1),'tip')
Quality.automf(3)
Service.automf(3)
tip['low'] = fuzzy.trimf(tip.universe,(0,0,13))
tip['medium'] = fuzzy.trimf(tip.universe,(0,13,25))
tip['high'] = fuzzy.trimf(tip.universe,(13,25,25))
Quality['average'].view()
Service.view()
tip.view()
Rule1=ctrl.Rule(Quality['poor'] & Service['poor'],tip['low'])
Rule1.view()
Tipping_ctrl = ctrl.ControlSystem([Rule1])
Tipping = ctrl.ControlSystemSimulation(Tipping_ctrl)
Tipping.input['quality']= 2.5
Tipping.input['service']= 3.5
Tipping.compute()
print(Tipping.output['tip'])
tip.view(sim = Tipping) """
print("Helo")