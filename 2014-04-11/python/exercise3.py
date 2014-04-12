from exercise2 import *

''' COSTANTS '''

ROADCOL = [0.25,0.25,0.25]
SIDEWALKCOL = [0.75,0.75,0.75]
GRASSCOL = [0,0.7,0.1]
GARDENWALK = [0.93,0.83,0.71]

''' FUNCTIONS '''

def PARABOLA(t):
	return [t[0],t[0]*t[0]]

def PARABOLAHILL(size,top_size,h):
	x, y = size
	tx, ty = top_size
	parabola_curve = S(2)(y/(x*x))(MAP(PARABOLA)(INTERVALS(x)(int(x*5))))
	x_line = T(2)(y)(Q(x))
	y_line = R([1,2])(PI/2)(Q(y))
	hill_step = T(1)(y)(R([1,2])(PI/2)(JOIN([parabola_curve,x_line,y_line])))
	hill_top = T(3)(h)(S([1,2])([ty/y, tx/x])(hill_step))

	return JOIN([hill_step,hill_top])

def RECTHILL(size,top_size,h):
	x, y = size
	tx, ty = top_size
	hill_step = CUBOID(size)
	hill_top = T(3)(h)(CUBOID(top_size))

	return JOIN([hill_step,hill_top])

''' NEIGHBOURS AND LAND '''

terrain = T([1,2])([-15,6.20])(COLOR(GRASSCOL)(CUBOID([70,40,4])))

# ROAD

p_hill = PARABOLAHILL([4.0,8.0], [1.0,4.7], 0.3*9) 
r_hill = RECTHILL([4.0,12.0], [1.0,12.0], 0.3*9)
p_hill = COLOR(GRASSCOL)(R([1,2])(PI)(p_hill))
p_hill = T([1,2])([16.0,-0.8])(p_hill)
r_hill = COLOR(GRASSCOL)(R([1,2])(-PI/2)(r_hill))
r_hill = T([1,2])([16.0,-0.8])(r_hill)
c_hill = T([1,2])([16.0,-0.80])(COLOR(GRASSCOL)(CUBOID([12.0,1.0,0.3*9])))

s1_hill = RECTHILL([6.40,15.0], [2.5,15.0], 4)
s1_hill = COLOR(GRASSCOL)(R([1,2])(-PI/2)(s1_hill))
s1_hill = T([1,2])([-15,6.40])(s1_hill)

s2_hill = CUBOID([25.8,6.40,4])
s2_hill = COLOR(GRASSCOL)(s2_hill)
s2_hill = T(1)(29.20)(s2_hill)

bar = CUBOID([25.80+0.4,0.10,5.20])
bar = T([1,2])([29.20-0.40,-0.10])(bar)

sidewalk1 = T([1,2,3])([-15,0,-0.08])(COLOR(SIDEWALKCOL)(CUBOID([70,-8,0.08])))
sidewalk2 = T([1,2,3])([-15,-16,-0.08])(COLOR(SIDEWALKCOL)(CUBOID([70,-4,0.08])))
road = T([1,2,3])([-15,-8.0,-0.08])(COLOR(ROADCOL)(CUBOID([70,-8])))

# GARDEN

ex_circle = MAP(CIRCLE)(RECTDOMAIN([2.5,PI*2],[10,25]))
in_circle = MAP(CIRCLE)(RECTDOMAIN([1.5,PI*2],[10,25]))
circle = EXTRUDE(0.08)(DIFFERENCE([ex_circle,in_circle]))
circle = T([1,2,3])([29.20+0.5,20,4])(circle)

walk1 = CUBOID([1.0,20-2,0.08])
walk1 = T([1,3])([29.20,4])(walk1)

walk2 = CUBOID([25.80,6.40, 0.08])
walk2 = T([1,3])([29.20,4])(walk2)

gardenwalk = COLOR(GARDENWALK)(STRUCT([circle, walk1,walk2]))

# LAND

land = STRUCT([terrain,p_hill, r_hill,c_hill,s1_hill,s2_hill,sidewalk1,sidewalk2,bar,road,gardenwalk])

# BUILDINGS

neighbour1 = CUBOID([13,6,15.2])
neighbour2 = STRUCT([CUBOID([11,12,12]),T([1,2])([9,-2])(CUBOID([9,12,11]))])

estate = STRUCT([land, T(3)(4),weissenhof, T([1,2])([-7,30]), neighbour1, T(1)(30), neighbour2])

VIEW(estate)