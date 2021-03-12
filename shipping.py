#sal's shipping problem from Codecademy Learn Python Course

weight = 140

#ground shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
  print(cost_ground)
elif (weight > 2) and (weight <= 6):
  cost_ground = weight * 3 + 20
  print(cost_ground)
elif (weight > 6) and (weight <= 10):
  cost_ground = weight * 4 + 20
  print(cost_ground)
elif weight > 10:
  cost_ground = weight * 4.75 + 20
  print(cost_ground)

#ground shipping PREMIUM
cost_pGround = 125
print(cost_pGround)

#drone shipping (new)
if weight <= 2:
  cost_drone = weight * 4.5
  print(cost_drone)
elif (weight > 2) and (weight <= 6):
  cost_drone = weight * 9
  print(cost_drone)
elif (weight > 6) and (weight <= 10):
  cost_drone = weight * 12
  print(cost_drone)
elif weight > 10:
  cost_drone = weight * 14.25
  print(cost_drone)
