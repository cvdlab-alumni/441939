from pyplasm import * 

p_1dim = [-0.05,0.22,-0.05]	# Centep_col unidimensional pillar
p_col = RED
div_col = BLUE

'''
FLOOR0a
'''

# Floor 0 plan

f0a_plan_vertices = [
	[0,0],[29.20,0],[29.20,6.24],[0,6.24],            # Base
	[12.80,0], [12.80,-0.80],[16.0,-0.80],[16.0,0],   # For the left ramp
	[27.88,0],[27.88,-0.80],[28.88,-0.80],[28.88,0]]  # FOr the right ramp
f0a_plan_cells = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
f0a_plan = MKPOL([f0a_plan_vertices,f0a_plan_cells, None])

# Floor 0 pillars


front_pillars0a_x = QUOTE(p_1dim+([-2.80]+p_1dim)*4+[-6.72]+p_1dim+([-2.80]+p_1dim)*3)
front_pillars0a_y = QUOTE(p_1dim+[-5.60,-0.32])

rear_pillars0a_x = QUOTE(p_1dim+[-2.80]+p_1dim+[-25.44]+p_1dim)
rear_pillars0a_y = QUOTE([-0.32,-5.60]+p_1dim)

front_pillars0a = PROD([front_pillars0a_x, front_pillars0a_y])
rear_pillars0a = PROD([rear_pillars0a_x, rear_pillars0a_y])
pillars0a = COLOR(p_col)(STRUCT([front_pillars0a, rear_pillars0a]))

# Floor 0 divider

div0a_wall = COLOR(div_col)(PROD([QUOTE([-16.0,0.32]), Q(2.24)]))

# Floor 0a

floor0a = STRUCT([f0a_plan, pillars0a, div0a_wall])

'''
FLOOR0b
'''

# Eveleted (by 1.20 m) floor 0 plan

f0b_plan_vertices = [
	[0,0],[19.84,0],[19.84,2.80],[0,2.80],
	[19.84,9.4],[16.4,9.4],[16.4,2.80],
	[3.44,2.80],[3.44,9.4],[0,9.4],
	[1.20,0],[1.20,-1.20],[18.64,-1.20],[18.64,0]]
f0b_plan_cells = [[1,2,3,4],[3,5,6,7],[4,8,9,10],[11,12,13,14]]
f0b_plan = MKPOL([f0b_plan_vertices, f0b_plan_cells, None])

def circle(p):
	r, a = p
	return [r*COS(a),r*SIN(a)]

domain = PROD([INTERVALS(1.20)(10),INTERVALS(PI/2)(20)])
quarter = MAP(circle)(domain)
curve1 = R([1,2])(PI)(quarter)
curve2 = R([1,2])(-PI/2)(quarter)

f0b_plan = STRUCT([f0b_plan,T(1)(1.20),curve1,T(1)(17.44),curve2])

# Eleveted floor 0 pillars

pillars0b_x = QUOTE(p_1dim+([-2.80]+p_1dim)*2+[-6.72]+p_1dim+([-2.80]+p_1dim)*2)
pillars0b_y = QUOTE([-2.48]+p_1dim)
pillars0b = COLOR(p_col)(PROD([pillars0b_x, pillars0b_y]))

back_pillars0b_x = QUOTE(p_1dim+[-2.80]+p_1dim + [-12.96] + p_1dim+[-2.80]+p_1dim)
back_pillars0b_y = QUOTE([-9.08]+p_1dim)
back_pillars0b = COLOR(p_col)(PROD([back_pillars0b_x, back_pillars0b_y]))

# Dividing wall

center_div0b = 19.84/2-0.32/2
div0b_wall = COLOR(div_col)(T(2)(-1.20)(PROD([QUOTE([-center_div0b,0.32,-center_div0b]), Q(4)])))

#Floor 0

floor0b = T([1,2])([6.24,3.44])(STRUCT([f0b_plan,pillars0b, back_pillars0b, div0b_wall]))

'''
FLOOR0a + FLOOR0b = FLOOR0
'''

# floor0a = DIFFERENCE([floor0a, floor0b])    # Cut floor0a to fit floor0b
floor0b = T(3)(1.2)(floor0b)                  # Elevate floor0b
floor0 = STRUCT([floor0a,floor0b])

'''
FLOOR1
'''

# Floor 1 plan

f1_plan1 = T(2)(-0.80)(PROD([Q(29.20),Q(6.24+0.80)]))
f1_plan2 = PROD([QUOTE([-6.24,3.44,-12.96,3.44]),QUOTE([-6.24,6.60])])
f1_plan = STRUCT([f1_plan1,f1_plan2])

# Floor 1 pillars

pillars1_x = front_pillars0a_x
pillars1_y = QUOTE(p_1dim+[-5.60]+p_1dim)
pillars1 = COLOR(p_col)(PROD([pillars1_x, pillars1_y]))

back_pillars1_x = QUOTE([-6.24] + p_1dim+[-2.80]+p_1dim + [-12.96] + p_1dim+[-2.80]+p_1dim)
back_pillars1_y = QUOTE([-(9.08+3.44)]+p_1dim)
back_pillars1 = COLOR(p_col)(PROD([back_pillars1_x, back_pillars1_y]))

# Diving wall

div1_wall = COLOR(div_col)(T(2)(-0.80)(PROD([QUOTE([-16.0,0.32]), Q(6.24+0.80)])))

floor1 = STRUCT([f1_plan, pillars1, back_pillars1, div1_wall])

'''
ROOF
'''

pillars2_x = QUOTE(p_1dim+([-2.80]+p_1dim)*4+[-6.72]+p_1dim+([-2.80]+p_1dim)*3)
pillars2_y = QUOTE(p_1dim+[-5.60,-0.32])
pillars2 = COLOR(p_col)(PROD([pillars2_x, pillars2_y]))
back_pillars2 = back_pillars1
roof = STRUCT([f1_plan,pillars2,back_pillars2])

'''
ROOF COVER
'''

cover1 = T(2)(-0.80)(PROD([Q(29.20),Q(2.60)]))
cover2 = PROD([QUOTE([-6.24,3.44,-12.96,3.44]),QUOTE([-4.40,6.60+1.84])])
support = [0.32,-2.80,0.32]
cover3 = PROD([QUOTE([-6.24]+support+[-12.96]+support),QUOTE([-1.80,2.60])])
cover = STRUCT([cover1, cover2, cover3])

'''
FLOORS
'''

floors = STRUCT([floor0, T(3)(4.0), floor1, T(3)(4.0), roof, T(3)(3.20), cover])
building = floors

VIEW(building)