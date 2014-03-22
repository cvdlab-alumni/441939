from exercise2 import *

p_col = RED
div_col = BLUE

# Floor 0

floor0a = PROD([f0a_plan,Q(-4.0)])
pillars0a = COLOR(p_col)(PROD([pillars0a,Q(4-0.40)]))
floor0a = STRUCT([floor0a,pillars0a])


floor0b = PROD([f0b_plan,Q(-1.20)])
pillars0b = COLOR(p_col)(PROD([pillars0b,Q(4-1.2-0.40)]))
back_pillars0b = COLOR(p_col)(PROD([back_pillars0b, Q(4-1.2-0.40)]))
floor0b = T([1,2])([6.24,3.44])(STRUCT([floor0b,pillars0b,back_pillars0b]))

floor0 = STRUCT([floor0a,T(3)(1.2),floor0b])

# Floor 1

floor1 = PROD([f1_plan,Q(-0.4)])
pillars1 = COLOR(p_col)(PROD([pillars1,Q(4-0.40)]))
back_pillars1 = COLOR(p_col)(PROD([back_pillars1, Q(4-0.40)]))
floor1 = STRUCT([floor1,pillars1,back_pillars1])

# ROOF

roof = PROD([f1_plan,Q(-0.4)])
pillars2 = COLOR(p_col)(PROD([pillars2,Q(3.20-0.40)]))
back_pillars2 = COLOR(p_col)(PROD([back_pillars2, Q(3.20-0.40)]))
roof = STRUCT([roof,pillars2,back_pillars2])

# ROOF COVER

cover = PROD([cover,Q(-0.4)])

# 3D Model

floors = STRUCT([floor0,T(3)(4.0),floor1,T(3)(4.0),roof,T(3)(3.20),cover])

VIEW(floors)

