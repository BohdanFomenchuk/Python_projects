import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

x_food = np.arange(0, 11, 1)
x_service = np.arange(0, 11, 1)
x_tip = np.arange(0, 21, 1)

# Food quality
y_food_bad = fuzz.trimf(x_food, [0, 0, 5])
y_food_decent = fuzz.trimf(x_food, [0, 5, 10])
y_food_great = fuzz.trimf(x_food, [5, 10, 10])

# Visualization
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x_food, y_food_bad, 'b', label='bad')
ax.plot(x_food, y_food_decent, 'g', label='decent')
ax.plot(x_food, y_food_great, 'r', label='great')
ax.set_title('Food quality')
ax.legend()

# Service quality
y_service_bad = fuzz.trimf(x_service, [0, 0, 5])
y_service_decent = fuzz.trimf(x_service, [0, 5, 10])
y_service_great = fuzz.trimf(x_service, [5, 10, 10])

# Visualization
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x_service, y_service_bad, 'b', label='bad')
ax.plot(x_service, y_service_decent, 'g', label='decent')
ax.plot(x_service, y_service_great, 'r', label='great')
ax.set_title('Service quality')
ax.legend()

# Tip
y_tip_low = fuzz.trimf(x_tip, [0, 0, 10])
y_tip_medium = fuzz.trimf(x_tip, [0, 10, 20])
y_tip_high = fuzz.trimf(x_tip, [10, 20, 20])

# Visualization
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x_tip, y_tip_low, 'b', label='low')
ax.plot(x_tip, y_tip_medium, 'g', label='medium')
ax.plot(x_tip, y_tip_high, 'r', label='high')
ax.set_title('Tip')
ax.legend()

# Inputs
food_level_bad = fuzz.interp_membership(x_food, y_food_bad, 8.0)
food_level_decent = fuzz.interp_membership(x_food, y_food_decent, 8.0)
food_level_great = fuzz.interp_membership(x_food, y_food_great, 8.0)

service_level_bad = fuzz.interp_membership(x_service, y_service_bad, 6.5)
service_level_decent = fuzz.interp_membership(x_service, y_service_decent, 6.5)
service_level_great = fuzz.interp_membership(x_service, y_service_great, 6.5)

# Rules
activation_rule1 = np.fmax(food_level_bad, service_level_bad)
activation_tip_low = np.fmin(activation_rule1, y_tip_low)
activation_tip_medium = np.fmin(service_level_decent, y_tip_medium)
activation_rule3 = np.fmax(service_level_great, food_level_great)
activation_tip_high = np.fmin(activation_rule3, y_tip_high)

# Visualization
x_tip0 = np.zeros_like(x_tip)
fig, ax = plt.subplots(figsize=(8, 5))
ax.fill_between(x_tip, x_tip0, activation_tip_low, facecolor='b')
ax.plot(x_tip, y_tip_low, 'b')
ax.fill_between(x_tip, x_tip0, activation_tip_medium, facecolor='g')
ax.plot(x_tip, y_tip_medium, 'g')
ax.fill_between(x_tip, x_tip0, activation_tip_high, facecolor='r')
ax.plot(x_tip, y_tip_high, 'r')

# Defuzzification
control = np.fmax(activation_tip_low, np.fmax(activation_tip_medium, activation_tip_high))
# tip = fuzz.defuzz(x_tip, control, 'centroid')
# tip = fuzz.defuzz(x_tip, control, 'bisector')
# tip = fuzz.defuzz(x_tip, control, 'mom')
# tip = fuzz.defuzz(x_tip, control, 'som')
tip = fuzz.defuzz(x_tip, control, 'lom')
tip_activation = fuzz.interp_membership(x_tip, control, tip)

# Visualization
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x_tip, y_tip_low, 'b')
ax.plot(x_tip, y_tip_medium, 'g')
ax.plot(x_tip, y_tip_high, 'r')
ax.fill_between(x_tip, x_tip0, control, facecolor='purple')
ax.plot([tip, tip], [0, tip_activation], 'black')
ax.set_title('Defuzzification')
plt.show()
