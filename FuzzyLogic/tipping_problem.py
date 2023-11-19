import skfuzzy as fuzz
import numpy as np
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

food = ctrl.Antecedent(np.arange(0, 11, 1), 'food')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
tip = ctrl.Consequent(np.arange(0, 21, 1), 'tip')

# Membership function
food.automf(number=3, names=['bad', 'decent', 'great'])
service.automf(number=3, names=['bad', 'decent', 'great'])

tip['low'] = fuzz.sigmf(tip.universe, 5, -1)
tip['medium'] = fuzz.gaussmf(tip.universe, 10, 3)
tip['high'] = fuzz.pimf(tip.universe, 10, 20, 20, 21)


# Rules
rule1 = ctrl.Rule(food['bad'] & service['bad'], tip['low'])
rule2 = ctrl.Rule(service['decent'] & food['decent'], tip['medium'])
rule3 = ctrl.Rule(service['great'] & food['great'], tip['high'])

# Control system
control_system = ctrl.ControlSystem([rule1, rule2, rule3])
fuzzy_system = ctrl.ControlSystemSimulation(control_system)

# Testing
fuzzy_system.input['food'] = 2
fuzzy_system.input['service'] = 4

fuzzy_system.compute()
print(fuzzy_system.output['tip'])
tip.view(sim=fuzzy_system)
plt.show()
