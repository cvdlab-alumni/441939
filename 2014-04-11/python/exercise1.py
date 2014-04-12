from pyplasm import * 

''' COSTANTS '''

p_1dim = [-0.05,0.22,-0.05]	# Cented p_col unidimensional pillar
p_col = [0.21,0.45,0.87]
div_col = [0.8,0.34,0.09]
div2_col = [0.62,0.73, 0.92]
covers_col = [0.74,0.73,0.73]
steps_col = [0.81,0.55,0.09]

''' FUNCTIONS '''

def EXTRUDE(h):
	def EXTRUDE0(obj2D):
		return PROD([obj2D,Q(h)])
	return EXTRUDE0

def QPRODS(qlist):
	quotes = [QUOTE(q) for q in qlist]
	if (len(qlist)==2):
		return PROD(quotes)
	return INSL(PROD)(quotes)

def CIRCLE(p):
	r, a = p
	return [r*COS(a),r*SIN(a)]

def RECTDOMAIN(size, shape):
	return PROD([INTERVALS(size[0])(shape[0]),INTERVALS(size[1])(shape[1])])

def RAMP(params):
	w,l,h,n,h_step = params
	steps = []
	covers = []
	for i in xrange(n):
		step = MKPOL([[[i*l,0],[(i+1)*l,0],[(i+1)*l,h*(i+1)-h_step],[i*l,h*(i+1)-h_step]],[[1,2,3,4]],None])
		cover = MKPOL([[[i*l-h_step,h*(i+1)-h_step],[(i+1)*l,h*(i+1)-h_step],[(i+1)*l,h*(i+1)],[i*l-h_step,h*(i+1)]],
			[[1,2,3,4]],None])
		steps = steps+[step]
		covers = covers+[cover]
	return EXTRUDE(w)(STRUCT(steps)), EXTRUDE(w)(STRUCT(covers))

''' FLOOR0A '''

# PLANT
f0a_plan = MKPOL([[[0,0],[29.20,0],[29.20,6.24],[0,6.24]],[[1,2,3,4]], None])
f0a_plan = STRUCT([T(3)(-0.02)(EXTRUDE(-4+0.02)(f0a_plan)), COLOR(covers_col)(EXTRUDE(-0.02)(f0a_plan))])

# DIVISION WALL
div0a_wall = COLOR(div_col)(QPRODS([[-16.0+0.32/2,0.32],[2.24],[4-0.40]]))

# PILLARS
front_pillars0a_x = QUOTE(p_1dim+([-2.80]+p_1dim)*4+[-6.72]+p_1dim+([-2.80]+p_1dim)*3)
front_pillars0a_y = QUOTE(p_1dim+[-5.60,-0.32])

rear_pillars0a_x = QUOTE(p_1dim+[-2.80]+p_1dim+[-25.44]+p_1dim)
rear_pillars0a_y = QUOTE([-0.32,-5.60]+p_1dim)

front_pillars0a = PROD([front_pillars0a_x, front_pillars0a_y])
rear_pillars0a = PROD([rear_pillars0a_x, rear_pillars0a_y])
pillars0a = STRUCT([front_pillars0a, rear_pillars0a])

pillars0a = COLOR(p_col)(EXTRUDE(4-0.40)(pillars0a))

# LEFT RAMP
land_ramp1 = MKPOL([[[12.80,0],[12.80,-0.80],[16.0,-0.80],[16.0,0]],[[1,2,3,4]], None])
land_ramp1_wall = land_ramp1
land_ramp1 = COLOR(covers_col)(EXTRUDE(-0.02)(land_ramp1))
land_ramp1_wall = COLOR(steps_col)(T(3)(-0.02)(EXTRUDE(-4+0.02)(land_ramp1_wall)))

steps1, covers1 = RAMP([0.80,0.3,0.25,16,0.02])
steps1 = COLOR(steps_col)(T([1,3])([8,-4.0])(R([2,3])(PI/2)(steps1)))
covers1 = COLOR(covers_col)(T([1,3])([8,-4.0])(R([2,3])(PI/2)(covers1)))

ramp1 = STRUCT([land_ramp1,land_ramp1_wall,steps1,covers1])

# RIGHT RAMP
land_ramp2 = MKPOL([[[27.88,0],[27.88,-0.80],[28.88,-0.80],[28.88,0]],[[1,2,3,4]], None])
land_ramp2_wall = land_ramp2
land_ramp2 = COLOR(covers_col)(EXTRUDE(-0.02)(land_ramp2))
land_ramp2_wall = COLOR(steps_col)(T(3)(-0.02)(EXTRUDE(-4+0.02)(land_ramp2_wall)))

steps2, covers2 = RAMP([1.0,0.3,0.25,16,0.02])
steps2 = COLOR(steps_col)(T([1,2,3])([27.88,-4.8-0.80,-4.0])(R([1,2])(PI/2)(R([2,3])(PI/2)(steps2))))
covers2 = COLOR(covers_col)(T([1,2,3])([27.88,-4.8-0.80,-4.0])(R([1,2])(PI/2)(R([2,3])(PI/2)(covers2))))

ramp2 = STRUCT([land_ramp2,land_ramp2_wall,steps2,covers2])

# INNDER LEFT RAMP
land_ramp3_wall = T([1,2])([6.24-0.8,3.44+1.40])(CUBOID([0.8,1,1.2-0.02]))
land_ramp3 = T([1,2,3])([6.24-0.8,3.44+1.40,1.2-0.02])(CUBOID([0.8,1,0.02]))
land_ramp3_wall = COLOR(steps_col)(land_ramp3_wall)
land_ramp3 = COLOR(covers_col)(land_ramp3)

steps3, covers3 = RAMP([1.0,0.2,0.3,4,0.02])
steps3 = COLOR(steps_col)(T([1,2])([6.24-1.6,3.44+1.40+1])(R([2,3])(PI/2)(steps3)))
covers3 = COLOR(covers_col)(T([1,2])([6.24-1.6,3.44+1.40+1,1.2-0.02])(R([2,3])(PI/2)(covers3)))

ramp3 = STRUCT([land_ramp3_wall, land_ramp3, steps3, covers3])

# INNER RIGHT RAMP
land_ramp4_wall = T(1)(19.44+0.8+0.4)(land_ramp3_wall)
land_ramp4 = T(1)(19.44+0.80+0.4)(land_ramp3)
land_ramp4_wall = COLOR(steps_col)(land_ramp4_wall)
land_ramp4 = COLOR(covers_col)(land_ramp4)

steps4, covers4 = RAMP([1.0,0.2,0.3,4,0.02])
steps4 = COLOR(steps_col)(T([1,2])([19.44+6.24+2,3.44+1.40])(R([1,2])(PI)(R([2,3])(PI/2)(steps4))))
covers4 = COLOR(covers_col)(T([1,2])([19.44+6.24+2,3.44+1.40])(R([1,2])(PI)(R([2,3])(PI/2)(covers4))))

ramp4 = STRUCT([land_ramp4_wall, land_ramp4, steps4, covers4])

# STRUCT
floor0a = STRUCT([f0a_plan, div0a_wall, pillars0a, ramp1, ramp2, ramp3, ramp4])

''' FLOOR0B '''

# PLANT
f0b_plan_vertices = [[0,0],[19.84,0],[19.84,2.80],[0,2.80],
	[19.84,9.4],[16.4,9.4],[16.4,2.80],
	[3.44,2.80],[3.44,9.4],[0,9.4],
	[1.20,0],[1.20,-1.20],[18.64,-1.20],[18.64,0]]
f0b_plan_cells = [[1,2,3,4],[3,5,6,7],[4,8,9,10],[11,12,13,14]]
f0b_plan = MKPOL([f0b_plan_vertices, f0b_plan_cells, None])

quarter = MAP(CIRCLE)(RECTDOMAIN([1.20,PI/2],[5,15]))
curve1 = R([1,2])(PI)(quarter)
curve2 = R([1,2])(-PI/2)(quarter)
f0b_plan = STRUCT([f0b_plan,T(1)(1.20),curve1,T(1)(17.44),curve2])

f0b_plan = EXTRUDE(-1.20)(f0b_plan)

# DIVISION WALL
center_div0b = 19.84/2-0.32
div0b_wall = T(2)(-1.20)(PROD([QUOTE([-center_div0b,0.32,-center_div0b]), Q(4-0.4)]))
div0b_wall = COLOR(div_col)(PROD([div0b_wall, Q(4-1.2-0.40)]))

# PILLARS
pillars0b_x = QUOTE(p_1dim+([-2.80]+p_1dim)*2+[-6.72]+p_1dim+([-2.80]+p_1dim)*2)
pillars0b_y = QUOTE([-2.48]+p_1dim)
pillars0b = PROD([pillars0b_x, pillars0b_y])

back_pillars0b_x = QUOTE(p_1dim+[-2.80]+p_1dim + [-12.96] + p_1dim+[-2.80]+p_1dim)
back_pillars0b_y = QUOTE([-9.08]+p_1dim)
back_pillars0b = PROD([back_pillars0b_x, back_pillars0b_y])

pillars0b = COLOR(p_col)(PROD([pillars0b,Q(4-1.2-0.40)]))
back_pillars0b = COLOR(p_col)(PROD([back_pillars0b, Q(4-1.2-0.40)]))

# INNERWALLS
inner_thickness = 0.20

#STRUCT
floor0b = T([1,2,3])([6.24,3.44,1.2])(STRUCT([f0b_plan,div0b_wall, pillars0b, back_pillars0b]))

''' FLOOR0 '''
floor0 = STRUCT([floor0a,floor0b])

'''FLOOR1'''

# PLAN
f1_plan1 = T(2)(-0.80)(PROD([Q(29.20),Q(6.24+0.80)]))
f1_plan2 = PROD([QUOTE([-6.24,3.44,-12.96,3.44]),QUOTE([-6.24,6.60])])
f1_plan = STRUCT([f1_plan1,f1_plan2])
f1_plan = EXTRUDE(-0.4)(f1_plan)

# PILLARS
pillars1_x = front_pillars0a_x
pillars1_y = QUOTE(p_1dim+[-5.60]+p_1dim)
pillars1 = PROD([pillars1_x, pillars1_y])

back_pillars1_x = QUOTE([-6.24] + p_1dim+[-2.80]+p_1dim + [-12.96] + p_1dim+[-2.80]+p_1dim)
back_pillars1_y = QUOTE([-(9.08+3.44)]+p_1dim)
back_pillars1 = PROD([back_pillars1_x, back_pillars1_y])

pillars1 = COLOR(p_col)(PROD([pillars1,Q(4-0.40)]))
back_pillars1 = COLOR(p_col)(PROD([back_pillars1, Q(4-0.40)]))

# DIVIDING WALL
div1_wall = T(2)(-0.80)(PROD([QUOTE([-16.0+0.32/2,0.32]), QUOTE([-0.4,6.24,-0.4])]))
div1_wall = COLOR(div_col)(PROD([div1_wall, Q(4-0.40)]))

# STRUCT
floor1 = STRUCT([f1_plan, pillars1, back_pillars1, div1_wall])

''' ROOF '''

# PLAN
roof_plan = f1_plan

# PILLARS
pillars2_x = QUOTE(p_1dim+([-2.80]+p_1dim)*4+[-6.72]+p_1dim+([-2.80]+p_1dim)*3)
pillars2_y = QUOTE(p_1dim+[-5.60,-0.32])
pillars2 = PROD([pillars2_x, pillars2_y])

back_pillars2_x = QUOTE([-6.24] + p_1dim+[-2.80]+p_1dim + [-12.96] + p_1dim+[-2.80]+p_1dim)
back_pillars2_y = QUOTE([-(9.08+3.44)]+p_1dim)
back_pillars2 = PROD([back_pillars2_x, back_pillars2_y])

pillars2 = COLOR(p_col)(PROD([pillars2,Q(3.20-0.40)]))
back_pillars2 = COLOR(p_col)(PROD([back_pillars2, Q(3.20-0.40)]))

# DIVIDING WALL
div2_wall = T(2)(-0.80)(PROD([QUOTE([-16.0+0.32/2,0.32]), QUOTE([-0.4,6.24,-0.4])]))
div2_wall = COLOR(div2_col)(EXTRUDE(3.20-0.40)(div2_wall))

# STRUCT
roof = STRUCT([roof_plan, pillars2,back_pillars2, div2_wall])

''' COVER '''

cover1 = T(2)(-0.80)(PROD([Q(29.20),Q(2.60)]))
cover2 = PROD([QUOTE([-6.24,3.44,-12.96,3.44]),QUOTE([-4.40,6.60+1.84])])
support = [0.32,-2.80,0.32]
cover3 = PROD([QUOTE([-6.24]+support+[-12.96]+support),QUOTE([-1.80,2.60])])

cover = STRUCT([cover1, cover2, cover3])
cover = EXTRUDE(-0.4)(cover)

''' 3D FLOORS '''
floors = STRUCT([floor0,T(3)(4.0),floor1,T(3)(4.0),roof, T(3)(3.2)(cover)])
# VIEW(floors)