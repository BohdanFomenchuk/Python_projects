import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

surface = ctrl.Antecedent(np.arange(0, 6, 1), 'surface')
dirt = ctrl.Antecedent(np.arange(0, 6, 1), 'dirt')
suction = ctrl.Consequent(np.arange(0, 11, 1), 'suction')

# Membership function
surface.automf(number=3, names=['easy', 'moderate', 'hard'])
dirt.automf(number=3, names=['light', 'moderate', 'heavy'])

suction['low'] = fuzz.trimf(suction.universe, [0, 0, 5])
suction['medium'] = fuzz.trimf(suction.universe, [0, 5, 10])
suction['high'] = fuzz.trimf(suction.universe, [5, 10, 10])

# Rules
rule1 = ctrl.Rule(surface['easy'] & dirt['light'], suction['low'])
rule2 = ctrl.Rule(surface['moderate'] & dirt['light'], suction['medium'])
rule3 = ctrl.Rule(surface['hard'] | dirt['heavy'], suction['high'])

# Control system
control_system = ctrl.ControlSystem([rule1, rule2, rule3])
fuzzy_system = ctrl.ControlSystemSimulation(control_system)

# Testing
fuzzy_system.input['surface'] = 5
fuzzy_system.input['dirt'] = 5
fuzzy_system.compute()
print(fuzzy_system.output['suction'])
suction.view(sim=fuzzy_system)
plt.show()
